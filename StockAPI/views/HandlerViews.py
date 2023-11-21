from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from ..models import Handler
from ..serializers import HandlerSerializer

class HandlerListAPIView(APIView):
    
        def get(self, request, *args, **kwargs):
            '''
            List all the Handler items
            '''
            handlers = Handler.objects.all()
            serializer = HandlerSerializer(handlers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        # 2. Create
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
        
class HandlerDetailAPIView(APIView):
    def get_object(self, handler_id):
        '''
        Helper method to get the object with given handler_id, and user_id
        '''
        try:
            return Handler.objects.get(pk=handler_id)
        except Handler.DoesNotExist:
            return None
    
    # 3. Retrieve
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
    def delete(self, request, handler_id, *args, **kwargs):
        '''
        Delete the Handler with given handler_id
        '''
        handler = self.get_object(handler_id)
        if handler is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        handler.delete()
        return Response(status=status.HTTP_200_OK)