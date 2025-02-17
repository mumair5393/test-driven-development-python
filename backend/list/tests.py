from django.test import TestCase
from django.urls import resolve
from list.views import home_page
from list.models import Item

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'List item one'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'List item two'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].text, 'List item one')
        self.assertEqual(saved_items[1].text, 'List item two')
        
        
        
        