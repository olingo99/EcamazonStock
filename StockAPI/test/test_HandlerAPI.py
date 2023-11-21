from django.test import TestCase
from ..models import Handler
import json

class HandlerListAPITests(TestCase):
    def test_create_handler(self):
        response = self.client.post('/StockAPI/handler', {
            'HandlerName': 'TestHandlerName',
            'HandlerSurname': 'TestHandlerSurname',
            'HandlerAddress': 'TestHandlerAddress'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Handler.objects.count(), 1)
        self.assertEqual(Handler.objects.get().HandlerName, 'TestHandlerName')
        self.assertEqual(Handler.objects.get().HandlerSurname, 'TestHandlerSurname')
        self.assertEqual(Handler.objects.get().HandlerAddress, 'TestHandlerAddress')

    def test_get_handlers(self):
        for _ in range(5):
            Handler.objects.create(
                HandlerName='TestHandlerName',
                HandlerSurname='TestHandlerSurname',
                HandlerAddress='TestHandlerAddress'
            )
        response = self.client.get('/StockAPI/handler')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['HandlerName'], 'TestHandlerName')
        self.assertEqual(response.data[0]['HandlerSurname'], 'TestHandlerSurname')
        self.assertEqual(response.data[0]['HandlerAddress'], 'TestHandlerAddress')

    def test_get_handlers_not_found(self):
        response = self.client.get('/StockAPI/handler')
        self.assertEqual(response.status_code, 200)

class HandlerDetailAPITests(TestCase):
    
        def test_get_handler(self):
            for _ in range(5):
                Handler.objects.create(
                    HandlerName='TestHandlerName',
                    HandlerSurname='TestHandlerSurname',
                    HandlerAddress='TestHandlerAddress'
                )
            response = self.client.get('/StockAPI/handler/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['HandlerName'], 'TestHandlerName')
            self.assertEqual(response.data['HandlerSurname'], 'TestHandlerSurname')
            self.assertEqual(response.data['HandlerAddress'], 'TestHandlerAddress')
    
        def test_get_handler_not_found(self):
            
            response = self.client.get('/StockAPI/handler/1')
    
            self.assertEqual(response.status_code, 404)
    
        def test_update_handler(self):
            Handler.objects.create(
                HandlerName='TestHandlerName',
                HandlerSurname='TestHandlerSurname',
                HandlerAddress='TestHandlerAddress'
            )
            response = self.client.put('/StockAPI/handler/1', {
                'HandlerName': 'TestHandlerNameUpdated',
                'HandlerSurname': 'TestHandlerSurnameUpdated',
                'HandlerAddress': 'TestHandlerAddressUpdated'
            },content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(Handler.objects.get().HandlerName, 'TestHandlerNameUpdated')
            self.assertEqual(Handler.objects.get().HandlerSurname, 'TestHandlerSurnameUpdated')
            self.assertEqual(Handler.objects.get().HandlerAddress, 'TestHandlerAddressUpdated')
    
        def test_update_handler_not_found(self):
            response = self.client.put('/StockAPI/handler/1', {
                'HandlerName': 'TestHandlerNameUpdated',
                'HandlerSurname': 'TestHandlerSurnameUpdated',
                'HandlerAddress': 'TestHandlerAddressUpdated'
            })
            self.assertEqual(response.status_code, 404)
    
        def test_delete_handler(self):
            Handler.objects.create(
                HandlerName='TestHandlerName',
                HandlerSurname='TestHandlerSurname',
                HandlerAddress='TestHandlerAddress'
            )
            response = self.client.delete('/StockAPI/handler/1')
            self.assertEqual(response.status_code, 200)
