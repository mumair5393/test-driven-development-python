import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME ,'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_user_flow(self):
        # User visits the website and notices "To-Do" in the title
        self.browser.get("http://localhost:8000")

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

        # There is still a text box inviting her to add another item. She # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        

        # There is still a text box inviting her to add another item. She 
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')
        # The page updates again, and now shows both items on her list

    
if __name__ == '__main__':
    unittest.main()
