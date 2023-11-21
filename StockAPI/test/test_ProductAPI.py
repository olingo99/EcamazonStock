# import datetime
# from django.test import TestCase
# from ..models import Product
# import json
# # Create your tests here.


# class ProductListAPITests(TestCase):
#     def test_create_product(self):
#         response = self.client.post('/StockAPI/product', {
#             'Quantity': 1,
#             'Location': 'testlocation',
#             'ProductName': 'testname'
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Product.objects.count(), 1)
#         self.assertEqual(Product.objects.get().Quantity, 1)
#         self.assertEqual(Product.objects.get().Location, 'testlocation')
#         self.assertEqual(Product.objects.get().ProductName, 'testname')


#     def test_get_products(self):
#         for _ in range(5):
#             Product.objects.create(
#                 ProductName='testname',
#                 Quantity=1,
#                 Location='testlocation',
#             )
#         response = self.client.get('/StockAPI/product')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 5)
#         self.assertEqual(response.data[0]['ProductName'], 'testname')
#         self.assertEqual(response.data[0]['Quantity'], 1)
#         self.assertEqual(response.data[0]['Location'], 'testlocation')
        

#     def test_get_products_not_found(self):
#         response = self.client.get('/StockAPI/product')
#         self.assertEqual(response.status_code, 200)

# class ProductDetailAPITests(TestCase):

#     def test_get_product(self):
#         for _ in range(5):
#             Product.objects.create(
#                 Name='testname',
#                 User=self.user
#             )
#         response = self.client.get('/SmartGalleryAPI/ProductApi/1')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['Name'], 'testname')
#         self.assertEqual(response.data['User'], self.user.id)

#     def test_get_product_not_found(self):
        
#         response = self.client.get('/SmartGalleryAPI/ProductApi/1')

#         self.assertEqual(response.status_code, 400)

#     def test_delete_product(self):
#         for _ in range(5):
#             Product.objects.create(
#                 Name='testname',
#                 User=self.user
#             )
#         response = self.client.delete('/SmartGalleryAPI/ProductApi/1')
#         self.assertEqual(response.status_code, 200)

#     def test_delete_product_not_found(self):
#         response = self.client.delete('/SmartGalleryAPI/ProductApi/1')
#         self.assertEqual(response.status_code, 400)

#     def test_update_product(self):
#         Product.objects.create(
#             Name='testname',
#             User=self.user
#         )
#         response = self.client.put('/SmartGalleryAPI/ProductApi/1', {
#             'Name': 'testname2',
#         },content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Product.objects.get().Name, 'testname2')