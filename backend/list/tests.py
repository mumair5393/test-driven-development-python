from django.test import TestCase
from django.urls import resolve
from list.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
        