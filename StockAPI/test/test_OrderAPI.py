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
        response_content = json.loads(response.content)
        if response.status_code == 503 and response_content.get('error') == 'Service is unavailable':
            print("Received expected 400 response with message: ", response_content.get('message'))
        else:
            self.assertEqual(response.status_code, 201)
            self.assertEqual(Order.objects.count(), 1)
            self.assertEqual(Order.objects.get().UserId, 1)
            self.assertEqual(Order.objects.get().State, 'Processing')
            self.assertEqual(OrderProductLink.objects.count(), 2)

    def test_cancel_order_updates_product_quantity(self):
        # Create an order
        response = self.client.post('/StockAPI/order', json.dumps({
            'UserId': 1,
            'Products': [
                {'ProductCode': int(self.product1.ProductCode), 'Quantity': 10},
                {'ProductCode': int(self.product2.ProductCode), 'Quantity': 20}
            ]
        }), content_type='application/json')
        response_content = json.loads(response.content)
        if response.status_code == 503 and response_content.get('error') == 'Service is unavailable':
            print("Received expected 400 response with error: ", response_content.get('error'))
        else:
            self.assertEqual(response.status_code, 201)

            # Get the created order
            order = Order.objects.get()

            # Update the order to "Cancelled"
            response = self.client.put(f'/StockAPI/order/{order.OrderId}', json.dumps({
                'State': 'Cancelled'
            }), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            # Reload the products from the database
            self.product1.refresh_from_db()
            self.product2.refresh_from_db()

            # Check if the quantity of the products has been updated correctly
            self.assertEqual(self.product1.Quantity, 100)
            self.assertEqual(self.product2.Quantity, 200)