from selenium import webdriver
import unittest


class NewUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_flow(self):
        # User visits the website and notices "To-Do" in the title
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)

        # Currently there is only a text box with an add button with it
        # User adds Task 1 and click add button.


        # User sees one Task 1 in the to-do list and also the text box
        # with an add button

        # Now there should be single to-do item
        # User adds Task 2 and click add button.
        self.fail("Finish the test!")

if __name__ == '__main__':
    unittest.main()
