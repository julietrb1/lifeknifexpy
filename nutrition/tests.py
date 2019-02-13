from django.contrib.auth.models import User
from django.test import TestCase

from nutrition.models import Food


class NutritionTests(TestCase):

    def setUp(self):
        User.objects.create(username='test', password='pass')

    def test_create_food(self):
        self.client.login(username='test', password='pass')
        food_to_create = {
            'name': 'testfood',
            'healthIndex': 1
        }
        response = self.client.post('/foods/', food_to_create)
        self.assertEqual(response.status_code, 201)
        foods = Food.objects.all()
        self.assertEqual(foods.length, 1)
        self.assertEqual(foods[0].name, food_to_create['name'])
