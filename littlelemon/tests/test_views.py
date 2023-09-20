from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
import json


class MenuViewTest(TestCase): 
    def setUp(self): 
        self.url = reverse("restaurant:menu")
        self.menu = Menu.objects.create(
            title = "Pasta",
            price = 20.00,
            inventory=10,
        )
        self.menu1 = Menu.objects.create(
            title="Pizza",
            price = 15.00,
            inventory = 10,
        )


    def test_getall(self):
        menu =[{"id":2,"title":"Pasta","price":'20.00',"inventory":10,},{"id":3,"title":"Pizza","price":'15.00',"inventory":10}]
        resp = self.client.get(self.url)

        self.assertListEqual(menu, json.loads(resp.content))
