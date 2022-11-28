from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Create your tests here.
# class PlayerFormTest(LiveServerTestCase):
#     def testform(self):
#         selenium = webdriver.Firefox()
#         # Choose your url to visit
#         selenium.get('http://127.0.0.1:8000/members/login_user')
#         # find the elements you need to submit form
#         username = selenium.find_element(By.ID, 'username')
#         password = selenium.find_element(By.ID, 'password')
#
#         submit = selenium.find_element(By.ID, 'submit')
#
#         # populate the form with data
#         username.send_keys('privetdek16@gmail.com')
#         password.send_keys('12334')
#
#         # submit form
#         submit.send_keys(Keys.RETURN)
#
#         time.sleep(0.5)
#
#         error_message = selenium.find_element(By.ID, 'error')
#
#         # check result; page source looks at entire html document
#         self.assertEqual(error_message.text, "Неверные данные")
#         # assert 'Неверные данные' in selenium.page_source
