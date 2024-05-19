from restaurant.models import Menu
from django.test import TestCase

class MenuItemTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(title='Ice Cream', price = 80, inventory = 100)
        self.assertEqual(str(item), 'Ice Cream : 80')