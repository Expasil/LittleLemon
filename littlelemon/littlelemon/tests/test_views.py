from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=200, inventory=50)

    def test_getall(self):
        # Make GET request to the menu-list endpoint
        response = self.client.get(reverse('menu'))

        # Retrieve all Menu objects
        items = Menu.objects.all()

        # Serialize the Menu objects
        serializer = MenuSerializer(items, many=True)

        # Assert that the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)