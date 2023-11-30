from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from ..models import Product
from ..serializers import ProductSerializer

class ProductListAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        '''
        List all the Product items
        '''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Product with given product data
        '''
        data = { 
            'Quantity':request.data.get('Quantity'),
            'ProductName':request.data.get('ProductName'),
            'CategoryId':request.data.get('CategoryId'),
            'WhareHouseId':request.data.get('WhareHouseId'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        '''
        Helper method to get the object with given product_id, and user_id
        '''
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None
    
    # 3. Retrieve
    def get(self, request, product_id, *args, **kwargs):
        '''
        Retrieve the Product with given product_id
        '''
        product = self.get_object(product_id)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 4. Update
    def put(self, request, product_id, *args, **kwargs):
        '''
        Update the Product with given product_id
        '''
        product = self.get_object(product_id)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = { 
            'Quantity':request.data.get('Quantity'),
            'ProductName':request.data.get('ProductName'),
            'CategoryId':request.data.get('CategoryId'),
            'WarehouseId':request.data.get('WarehouseId'),
        }
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    def delete(self, request, product_id, *args, **kwargs):
        '''
        Delete the Product with given product_id
        '''
        product = self.get_object(product_id)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProdcutFIlterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Filter the Product with given product data
        '''
        data = { 
            'Quantity':request.data.get('Quantity'),
            'ProductName':request.data.get('ProductName'),
            'CategoryId':request.data.get('CategoryId'),
            'WarehouseId':request.data.get('WarehouseId'),
        }
        data = {key: value for key, value in data.items() if value is not None and value != '' and value != "*"}
        
        products = Product.objects.filter(**data)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)