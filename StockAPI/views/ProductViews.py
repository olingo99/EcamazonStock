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
            'WarehouseId':request.data.get('WarehouseId'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)