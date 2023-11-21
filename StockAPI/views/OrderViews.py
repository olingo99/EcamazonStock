from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from ..models import Order
from ..serializers import OrderSerializer

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
    def post(self, request, *args, **kwargs):
        '''
        Create the Order with given order data
        '''
        data = { 
            'OrderDate':request.data.get('OrderDate'),
            'UserId':request.data.get('UserId'),
            'State':request.data.get('State'),
            'ParcelId':request.data.get('ParcelId')
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
    def put(self, request, productId, *args, **kwargs):
        '''
        Update the Order with given order_id
        '''
        order = self.get_object(productId)
        if not order:
            return Response(
                {'error': 'Order with id: {} does not exist'.format(productId)},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = { 
            'OrderDate':request.data.get('OrderDate'),
            'UserId':request.data.get('UserId'),
            'State':request.data.get('State'),
            'ParcelId':request.data.get('ParcelId')
        }
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
