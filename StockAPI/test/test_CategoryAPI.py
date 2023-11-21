from django.test import TestCase
from ..models import Category
import json


class CategoryListAPITests(TestCase):
    def test_create_category(self):
        response = self.client.post('/StockAPI/category', {
            'CategoryName': 'TestCategoryName',
            'CategoryDescription': 'TestCategoryDescription'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().CategoryName, 'TestCategoryName')
        self.assertEqual(Category.objects.get().CategoryDescription, 'TestCategoryDescription')

    def test_get_categorys(self):
        for _ in range(5):
            Category.objects.create(
                CategoryName='TestCategoryName',
                CategoryDescription='TestCategoryDescription'
            )
        response = self.client.get('/StockAPI/category')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['CategoryName'], 'TestCategoryName')
        self.assertEqual(response.data[0]['CategoryDescription'], 'TestCategoryDescription')

    def test_get_categorys_not_found(self):
        response = self.client.get('/StockAPI/category')
        self.assertEqual(response.status_code, 200)


class CategoryDetailAPITests(TestCase):
        
            def test_get_category(self):
                for _ in range(5):
                    Category.objects.create(
                        CategoryName='TestCategoryName',
                        CategoryDescription='TestCategoryDescription'
                    )
                response = self.client.get('/StockAPI/category/1')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data['CategoryName'], 'TestCategoryName')
                self.assertEqual(response.data['CategoryDescription'], 'TestCategoryDescription')
        
            def test_get_category_not_found(self):
                
                response = self.client.get('/StockAPI/category/1')
        
                self.assertEqual(response.status_code, 404)
        
            def test_update_category(self):
                Category.objects.create(
                    CategoryName='TestCategoryName',
                    CategoryDescription='TestCategoryDescription'
                )
                response = self.client.put('/StockAPI/category/1', {
                    'CategoryName': 'TestCategoryNameUpdated',
                    'CategoryDescription': 'TestCategoryDescriptionUpdated'
                },content_type='application/json')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(Category.objects.get().CategoryName, 'TestCategoryNameUpdated')
                self.assertEqual(Category.objects.get().CategoryDescription, 'TestCategoryDescriptionUpdated')
        
            def test_update_category_not_found(self):
                response = self.client.put('/StockAPI/category/1', {
                    'CategoryName': 'TestCategoryNameUpdated',
                    'CategoryDescription': 'TestCategoryDescriptionUpdated'
                })
                self.assertEqual(response.status_code, 404)
        
            def test_delete_category(self):
                Category.objects.create(
                    CategoryName='TestCategoryName',
                    CategoryDescription='TestCategoryDescription'
                )
                response = self.client.delete('/StockAPI/category/1')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(Category.objects.count(), 0)
        
            def test_delete_category_not_found(self):
                response = self.client.delete('/StockAPI/category/1')
                self.assertEqual(response.status_code, 404)
