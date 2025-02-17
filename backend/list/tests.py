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
        
    def test_only_save_items_when_necessary(self):
        response = self.client.get('/')
        self.assertEqual(Item.objects.all().count(), 0)

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        
    def test_redirects_after_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], '/')
        
    def test_display_all_list_tems(self):
        Item.objects.create(text='itemey 1') 
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/')
        
        self.assertIn("itemey 1", response.content.decode() )
        self.assertIn("itemey 2", response.content.decode() )


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
        
        
        
        