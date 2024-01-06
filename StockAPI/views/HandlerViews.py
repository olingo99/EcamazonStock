from rest_framework.response import Response
from rest_framework import status
from ..models import Handler
from ..serializers import HandlerSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics

class HandlerListAPIView(generics.GenericAPIView):

    serializer_class = HandlerSerializer

    @extend_schema(operation_id='listHandlers', description='List all the Handler items')
    def get(self, request, *args, **kwargs):
        '''
        List all the Handler items
        '''
        handlers = Handler.objects.all()
        serializer = HandlerSerializer(handlers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @extend_schema(operation_id='createHandler', description='Create the Handler with given handler data')
    def post(self, request, *args, **kwargs):
        '''
        Create the Handler with given handler data
        '''
        data = { 
            'HandlerName':request.data.get('HandlerName'),
            'HandlerSurname':request.data.get('HandlerSurname'),
            'HandlerAddress':request.data.get('HandlerAddress')
        }
        serializer = HandlerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HandlerDetailAPIView(generics.GenericAPIView):
    serializer_class = HandlerSerializer


    def get_object(self, handler_id):
        '''
        Helper method to get the object with given handler_id, and user_id
        '''
        try:
            return Handler.objects.get(pk=handler_id)
        except Handler.DoesNotExist:
            return None
    
    
    # 3. Retrieve
    @extend_schema(operation_id='retrieveHandler', description='Retrieve the Handler with given handler_id')
    def get(self, request, handler_id, *args, **kwargs):
        '''
        Retrieve the Handler with given handler_id
        '''
        handler = self.get_object(handler_id)
        if handler is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HandlerSerializer(handler)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 4. Update
    @extend_schema(operation_id='updateHandler', description='Update the Handler with given handler_id')
    def put(self, request, handler_id, *args, **kwargs):
        '''
        Update the Handler with given handler_id
        '''
        handler = self.get_object(handler_id)
        if handler is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = { 
            'HandlerName':request.data.get('HandlerName'),
            'HandlerSurname':request.data.get('HandlerSurname'),
            'HandlerAddress':request.data.get('HandlerAddress')
        }
        serializer = HandlerSerializer(handler, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    @extend_schema(operation_id='deleteHandler', description='Delete the Handler with given handler_id')
    def delete(self, request, handler_id, *args, **kwargs):
        '''
        Delete the Handler with given handler_id
        '''
        handler = self.get_object(handler_id)
        if handler is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        handler.delete()
        return Response(status=status.HTTP_200_OK)