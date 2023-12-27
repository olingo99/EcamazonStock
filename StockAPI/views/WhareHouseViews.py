from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from ..models import WhareHouse
from ..serializers import WhareHouseSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics

class WhareHouseListAPIView(generics.GenericAPIView):
    serializer_class = WhareHouseSerializer

    @extend_schema(operation_id='listWhareHouses', description='List all the WhareHouse items')
    def get(self, request, *args, **kwargs):
        '''
        List all the WhareHouse items
        '''
        wharehouses = WhareHouse.objects.all()
        serializer = WhareHouseSerializer(wharehouses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @extend_schema(operation_id='createWhareHouse', description='Create the WhareHouse with given wharehouse data')
    def post(self, request, *args, **kwargs):
        '''
        Create the WhareHouse with given wharehouse data
        '''
        data = { 
            'WhareHouseName':request.data.get('WhareHouseName'),
            'WhareHouseLocation':request.data.get('WhareHouseLocation')
        }
        serializer = WhareHouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WhareHouseDetailAPIView(generics.GenericAPIView):
    serializer_class = WhareHouseSerializer

    def get_object(self, wharehouse_id):
        '''
        Helper method to get the object with given wharehouse_id, and user_id
        '''
        try:
            return WhareHouse.objects.get(pk=wharehouse_id)
        except WhareHouse.DoesNotExist:
            return None

    # 3. Retrieve
    @extend_schema(operation_id='retrieveWhareHouse', description='Retrieve the WhareHouse with given wharehouse_id')
    def get(self, request, wharehouse_id, *args, **kwargs):
        '''
        Retrieve the WhareHouse with given wharehouse_id
        '''
        wharehouse = self.get_object(wharehouse_id)
        if wharehouse is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WhareHouseSerializer(wharehouse)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    @extend_schema(operation_id='updateWhareHouse', description='Update the WhareHouse with given wharehouse_id')
    def put(self, request, wharehouse_id, *args, **kwargs):
        '''
        Update the WhareHouse with given wharehouse_id
        '''
        
        wharehouse = self.get_object(wharehouse_id)
        if wharehouse is None:
            # print("wharehouse not found")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WhareHouseSerializer(wharehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    @extend_schema(operation_id='deleteWhareHouse', description='Delete the WhareHouse with given wharehouse_id')
    def delete(self, request, wharehouse_id, *args, **kwargs):
        '''
        Delete the WhareHouse with given wharehouse_id
        '''
        wharehouse = self.get_object(wharehouse_id)
        if wharehouse is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        wharehouse.delete()
        return Response(status=status.HTTP_200_OK)
    
