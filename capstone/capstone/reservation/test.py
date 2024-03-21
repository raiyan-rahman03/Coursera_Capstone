from django.test import TestCase
from .models import *  # Assuming your model is named Menu, adjust the import accordingly

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a menu item
        item = menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        
        # Retrieve the item from the database
        retrieved_item = menu.objects.get(Title="IceCream")
        
        # Assert that the retrieved item matches the expected values
        self.assertEqual(retrieved_item.Title, "IceCream")
        self.assertEqual(retrieved_item.Price, 80)
        self.assertEqual(retrieved_item.Inventory, 100)
