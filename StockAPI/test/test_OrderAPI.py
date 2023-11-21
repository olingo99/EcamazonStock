from django.test import TestCase
from ..models import Order
import json

class OrderListAPITests(TestCase):
    def test_create_order(self):
        response = self.client.post('/StockAPI/order', {
            'OrderDate': '2020-01-01',
            'UserId': 1,
            'State': 'Sent',
            'ParcelId': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().OrderDate, '2020-01-01')
        self.assertEqual(Order.objects.get().UserId, 1)
        self.assertEqual(Order.objects.get().State, 'Sent')
        self.assertEqual(Order.objects.get().ParcelId, 1)

    def test_get_orders(self):
        for _ in range(5):
            Order.objects.create(
                OrderDate='2020-01-01',
                UserId=1,
                State='Sent',
                ParcelId=1
            )
        response = self.client.get('/StockAPI/order')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['UserId'], 1)
        self.assertEqual(response.data[0]['State'], 'Sent')
        self.assertEqual(response.data[0]['ParcelId'], 1)

    def test_get_orders_not_found(self):
        response = self.client.get('/StockAPI/order')
        self.assertEqual(response.status_code, 200)

class OrderDetailAPITests(TestCase):

    def test_get_order(self):
        for _ in range(5):
            Order.objects.create(
                OrderDate='2020-01-01',
                UserId=1,
                State='Sent',
                ParcelId=1
            )
        response = self.client.get('/StockAPI/order/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['UserId'], 1)
        self.assertEqual(response.data['State'], 'Sent')
        self.assertEqual(response.data['ParcelId'], 1)

    def test_get_order_not_found(self):
        
        response = self.client.get('/StockAPI/order/1')

        self.assertEqual(response.status_code, 400)

    def test_delete_order(self):
        for _ in range(5):
            Order.objects.create(
                OrderDate='2020-01-01',
                UserId=1,
                State='Sent',
                ParcelId=1
            )
        response = self.client.delete('/StockAPI/order/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_order_not_found(self):
        response = self.client.delete('/StockAPI/order/1')
        self.assertEqual(response.status_code, 400)

    def test_update_order(self):
        Order.objects.create(
            OrderDate='2020-01-01',
            UserId=1,
            State='Sent',
            ParcelId=1
        )
        response = self.client.put('/StockAPI/order/1', {
            'OrderDate': '2020-01-01',
            'UserId': 1,
            'State': 'Sent',
            'ParcelId': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.get().OrderDate, '2020-01-01')
        self.assertEqual(Order.objects.get().UserId, 1)
        self.assertEqual(Order.objects.get().State, 'Sent')
        self.assertEqual(Order.objects.get().ParcelId, 1)
        

    

        


