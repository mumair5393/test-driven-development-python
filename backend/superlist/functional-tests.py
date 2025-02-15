from django.template.defaultfilters import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_flow(self):
        # User visits the website and notices "To-Do" in the title
        self.browser.get("http://localhost:5173")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")
        
        # She enters the first to-do item
        input_box.send_keys("Buy peacock feathers.")
        
        # When she hits enter the page updates and now the page has a to-do item on the page.
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows) )
        

        # There is still a text box inviting her to add another item. She 
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')
        # The page updates again, and now shows both items on her list


if __name__ == '__main__':
    unittest.main()
