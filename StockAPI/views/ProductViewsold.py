# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # from rest_framework import permissions
# from ..models import Product
# from ..serializers import ProductSerializer


# class ProductListAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         '''
#         List all the Product items
#         '''
#         products = Product.objects.filter(ProductName__contains = "")
#         print(products)
#         products2 = Product.objects.all()
#         print(products2)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Product with given product data
#         '''
#         data = { 
#             'Quantity':request.data.get('Quantity'),
#             'Location':request.data.get('Location'),
#             'ProductName':request.data.get('ProductName')
#         }
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductFilterAPIView(APIView):
#     def get(self, request,querryString, *args, **kwargs):
#         '''
#         List all the Product items for given requested user
#         '''
#         products = Product.objects.filter(ProductName__contains = querryString)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class ProductDetailAPIView(APIView):
#     def get_object(self, product_id):
#         '''
#         Helper method to get the object with given product_id, and user_id
#         '''
#         try:
#             return Product.objects.get(pk=product_id)
#         except Product.DoesNotExist:
#             return None

#     # 3. Retrieve
#     def get(self, request, productId, *args, **kwargs):
#         '''
#         Retrieves the Product with given product_id
#         '''
#         product_instance = self.get_object(productId)
#         if not product_instance:
#             return Response(
#                 {"res": "Object with product id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = ProductSerializer(product_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 4. Update
#     def put(self, request, productId, *args, **kwargs):
#         '''
#         Updates the product item with given product_id if exists
#         '''
#         print("put")
#         product_instance = self.get_object(productId)
#         if not product_instance:
#             return Response(
#                 {"res": "Object with product id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'Path': request.data.get('Path'),
#             'Location': request.data.get('Location'),
#             'User': request.user.id,
#             'Date': request.data.get('Date')
#         }
#         serializer = ProductSerializer(instance = product_instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 5. Delete
#     def delete(self, request, productId, *args, **kwargs):
#         '''
#         Deletes the product item with given product_id if exists
#         '''
#         product_instance = self.get_object(productId)
#         if not product_instance:
#             return Response(
#                 {"res": "Object with product id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         product_instance.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )