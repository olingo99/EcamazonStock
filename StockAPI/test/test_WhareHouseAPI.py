from django.test import TestCase
from ..models import WhareHouse
from ..serializers import WhareHouseSerializer
import json

class WhareHouseListAPITests(TestCase):
    def test_create_wharehouse(self):
        response = self.client.post('/StockAPI/wharehouse', {
            'WhareHouseName': 'TestName',
            'WhareHouseLocation': 'TestLocation'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(WhareHouse.objects.count(), 1)
        self.assertEqual(WhareHouse.objects.get().WhareHouseName, 'TestName')
        self.assertEqual(WhareHouse.objects.get().WhareHouseLocation, 'TestLocation')

    def test_get_wharehouses(self):
        for _ in range(5):
            WhareHouse.objects.create(
                WhareHouseName='TestName',
                WhareHouseLocation='TestLocation'
            )
        response = self.client.get('/StockAPI/wharehouse')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['WhareHouseName'], 'TestName')
        self.assertEqual(response.data[0]['WhareHouseLocation'], 'TestLocation')


class WhareHouseDetailAPITests(TestCase):
    
        def test_get_wharehouse(self):
            for _ in range(5):
                WhareHouse.objects.create(
                    WhareHouseName='TestName',
                    WhareHouseLocation='TestLocation'
                )
            response = self.client.get('/StockAPI/wharehouse/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['WhareHouseName'], 'TestName')
            self.assertEqual(response.data['WhareHouseLocation'], 'TestLocation')
    
        def test_get_wharehouse_not_found(self):
            
            response = self.client.get('/StockAPI/wharehouse/1')
    
            self.assertEqual(response.status_code, 404)

        def test_update_wharehouse(self):
            WhareHouse.objects.create(
                WhareHouseName='TestName',
                WhareHouseLocation='TestLocation'
            )
            response = self.client.put('/StockAPI/wharehouse/1', {
                "WhareHouseName": "TestName2",
                "WhareHouseLocation": "TestLocation2"
            },content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(WhareHouse.objects.get().WhareHouseName, 'TestName2')
            self.assertEqual(WhareHouse.objects.get().WhareHouseLocation, 'TestLocation2')

        def test_update_wharehouse_not_found(self):
            # print("wharehouse put test not found")
            response = self.client.put('/StockAPI/wharehouse/1', {
                "WhareHouseName": "TestName2",
                "WhareHouseLocation": "TestLocation2"
            })
            self.assertEqual(response.status_code, 404)

        def test_delete_wharehouse(self):
            WhareHouse.objects.create(
                WhareHouseName='TestName',
                WhareHouseLocation='TestLocation'
            )
            response = self.client.delete('/StockAPI/wharehouse/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(WhareHouse.objects.count(), 0)
        

