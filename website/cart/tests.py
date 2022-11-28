from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Create your tests here.
class CartFormTest(LiveServerTestCase):
    def testRedirect(self):
        selenium = webdriver.Firefox()
        selenium.get('http://127.0.0.1:8000')
        button = selenium.find_element(By.NAME, '123')

        button.send_keys(Keys.RETURN)

        time.sleep(0.5)

        body = selenium.find_element(By.XPATH, "//td[@class='product-name']")

        self.assertEqual(body.text, "qweqwe")

