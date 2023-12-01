from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from ..models import Order, Product, OrderProductLink, Handler
from ..serializers import OrderSerializer, ProductSerializer
import hashlib
import random
from django.db.models import Count
from django.db.models.functions import Random

class OrderListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        List all the Orders
        '''
        orders = Order.objects.all()
        print(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Order with given order data
    #     '''
    #     data = { 
    #         'UserId':request.data.get('UserId'),
    #         'State':request.data.get('State'),
    #         'ParcelId':request.data.get('ParcelId')
    #     }
    #     serializer = OrderSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, *args, **kwargs):
        '''
        Create the Order with given order data
        '''
        user_id = request.data.get('UserId')
        products = request.data.get('Products')  # Expect a list of {'ProductCode': ..., 'Quantity': ...}

        # Create a new Order instance with default State
        order = Order(UserId=user_id, State="Processing", ParcelId=0)
        order.save()

        # Generate ParcelId
        orderCreationTime = order.OrderDate
        random_number = random.randint(0, 9999)  # Generate a random number between 0 and 9999
        raw_str = f"{orderCreationTime}{user_id}{order.OrderId}{random_number}"
        hashed_str = hashlib.sha256(raw_str.encode()).hexdigest()
        parcel_id = int(hashed_str, 16) % 10**8  # Take the first 8 digits
        order.ParcelId = parcel_id
        order.save()

        # Add products to the order
        for item in products:
            product = Product.objects.get(ProductCode=item['ProductCode'])
            if product.Quantity < item['Quantity']:
                return Response({"error": f"Not enough quantity for product {product.ProductCode}"}, status=status.HTTP_400_BAD_REQUEST)
            handler_count = Handler.objects.aggregate(count=Count('HandlerId'))['count']
            if handler_count > 0:
                product.Quantity -= item['Quantity']
                product.save()
                random_handler = Handler.objects.order_by('?').first()
                link = OrderProductLink(OrderId=order, ProductId=product, ProductQuantity=item['Quantity'], HandlerId=random_handler)
                link.save()
            else:
                return Response({"error": "No handlers available"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class OrderFilterAPIView(APIView):
    def get(self, request,querryString, *args, **kwargs):
        '''
        List all the Order items for given requested user
        '''
        orders = Order.objects.filter(State__contains = querryString)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderDetailAPIView(APIView):
    
    def get_object(self, order_id):
        '''
        Helper method to get the object with given order_id
        '''
        try:
            return Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return None
        
    # 3. Retrieve
    def get(self, request, orderId, *args, **kwargs):
        '''
        Retrieve the Order with given order_id
        '''
        order = self.get_object(orderId)
        if not order:
            return Response(
                {'error': 'Order with id: {} does not exist'.format(orderId)},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, orderId, *args, **kwargs):
        '''
        Update the Order with given order_id
        '''
        order = self.get_object(orderId)
        if not order:
            return Response(
                {'error': 'Order with id: {} does not exist'.format(orderId)},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the state is being updated to "Cancelled"
        if request.data.get('State') == 'Cancelled' and order.State != 'Cancelled':
            # Iterate over the OrderProductLink instances related to the order
            for link in order.orderproductlink_set.all():
                # Add the quantity of the product back to the Product instance
                product = link.ProductId
                product.Quantity += link.ProductQuantity
                product.save()

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 5. Delete
    def delete(self, request, orderId, *args, **kwargs):
        '''
        Delete the Order with given order_id
        '''
        order = self.get_object(orderId)
        if not order:
            return Response(
                {'error': 'Order with id: {} does not exist'.format(orderId)},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.delete()
        return Response(
            {'res': 'Order with id: {} deleted successfully'.format(orderId)},
            status=status.HTTP_200_OK
        )
