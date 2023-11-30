from django.test import TestCase
from ..models import Order, Product, WhareHouse, Category, OrderProductLink, Handler
import json

class OrderListAPITests(TestCase):
    def setUp(self):
        # self.client = APIClient()
        self.warehouse = WhareHouse.objects.create(WhareHouseName='Warehouse1', WhareHouseLocation='Location1')
        self.category = Category.objects.create(CategoryName='Category1', CategoryDescription='Description1')
        self.product1 = Product.objects.create(Quantity=100, ProductName='Product1', WhareHouseId=self.warehouse, CategoryId=self.category)
        self.product2 = Product.objects.create(Quantity=200, ProductName='Product2', WhareHouseId=self.warehouse, CategoryId=self.category)
        self.handler = Handler.objects.create(HandlerName='Handler1', HandlerSurname='Surname1', HandlerAddress='Address1')
        
    def test_create_order(self):
        response = self.client.post('/StockAPI/order', json.dumps({
            'UserId': 1,
            'Products': [
                {'ProductCode': int(self.product1.ProductCode), 'Quantity': 10},
                {'ProductCode': int(self.product2.ProductCode), 'Quantity': 20}
            ]
        }), content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().UserId, 1)
        self.assertEqual(Order.objects.get().State, 'Processing')
        self.assertEqual(OrderProductLink.objects.count(), 2)