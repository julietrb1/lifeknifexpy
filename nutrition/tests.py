from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from nutrition.models import Food

API_FOODS = '/foods/'


class NutritionTests(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create_user(username='test2', password='pass')
        self.c.force_authenticate(self.user)

    def test_create_food(self):
        food_to_create = {
            'name': 'testfood',
            'health_index': 1
        }
        response = self.c.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 201)
        foods = Food.objects.all()
        self.assertEqual(Food.objects.count(), 1)
        self.assertEqual(foods[0].name, food_to_create['name'])
        self.assertEqual(foods[0].health_index, food_to_create['health_index'])

    def test_create_food_health_index_too_high(self):
        food_to_create = {
            'name': 'testfood',
            'health_index': 5
        }
        response = self.c.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Food.objects.count(), 0)

    def test_create_food_health_index_too_low(self):
        food_to_create = {
            'name': 'testfood',
            'health_index': 0
        }
        response = self.c.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Food.objects.count(), 0)

    def test_create_food_health_index_missing(self):
        food_to_create = {
            'name': 'testfood',
        }
        response = self.c.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('health_index' in response.data, 'health_index not in response')
        self.assertEqual(len(response.data['health_index']), 1, 'unexpected number of errors')
        self.assertEqual(response.data['health_index'][0], 'This field is required.')
        self.assertEqual(Food.objects.count(), 0)

    def test_create_duplicate_food(self):
        food = Food.objects.create(name='testfood', health_index=1, owner=self.user)
        food_to_create = {
            'name': food.name,
            'health_index': 2
        }
        response = self.c.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 400)
        foods = Food.objects.all()
        self.assertEqual(Food.objects.count(), 1)
        self.assertEqual(foods[0].name, food.name)
        self.assertEqual(foods[0].health_index, food.health_index)

    def test_create_food_no_auth(self):
        food_to_create = {
            'name': 'testfood',
            'health_index': 1
        }
        response = self.client.post(API_FOODS, food_to_create)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Food.objects.count(), 0)

    def test_get_food(self):
        food = Food.objects.create(name='testfood', health_index=1, owner=self.user)
        response = self.c.get(f'{API_FOODS}{food.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], food.name)
        self.assertEqual(response.data['health_index'], food.health_index)

    def test_get_foreign_food(self):
        other_user = User.objects.create(username='other', password='pass')
        food = Food.objects.create(name='testfood', health_index=1, owner=other_user)
        response = self.c.get(f'{API_FOODS}{food.id}/')
        self.assertEqual(response.status_code, 404)

    def test_get_nonexistent_food(self):
        response = self.c.get(f'{API_FOODS}123/')
        self.assertEqual(response.status_code, 404)