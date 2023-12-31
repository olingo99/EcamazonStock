from rest_framework.response import Response
from rest_framework import status
from ..models import Category
from ..serializers import CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics

class CategoryListAPIView(generics.GenericAPIView):
    serializer_class = CategorySerializer

    @extend_schema(operation_id='listCategories', description='List all the Category items')
    def get(self, request, *args, **kwargs):
        '''
        List all the Category items
        '''
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @extend_schema(operation_id='createCategory', description='Create the Category with given category data')
    def post(self, request, *args, **kwargs):
        '''
        Create the Category with given category data
        '''
        data = { 
            'CategoryName':request.data.get('CategoryName'),
            'CategoryDescription':request.data.get('CategoryDescription')
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get_object(self, category_id):
        '''
        Helper method to get the object with given category_id, and user_id
        '''
        try:
            return Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return None
        
    # 3. Retrieve
    @extend_schema(operation_id='retrieveCategory', description='Retrieve the Category with given category_id')
    def get(self, request, category_id, *args, **kwargs):
        '''
        Retrieve the Category with given category_id
        '''
        category = self.get_object(category_id)

        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 4. Update
    @extend_schema(operation_id='updateCategory', description='Update the Category with given category_id')
    def put(self, request, category_id, *args, **kwargs):
        '''
        Update the Category with given category_id
        '''
        category = self.get_object(category_id)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {
            'CategoryName':request.data.get('CategoryName'),
            'CategoryDescription':request.data.get('CategoryDescription')
        }
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    @extend_schema(operation_id='deleteCategory', description='Delete the Category with given category_id')
    def delete(self, request, category_id, *args, **kwargs):
        '''
        Delete the Category with given category_id
        '''
        category = self.get_object(category_id)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_200_OK)