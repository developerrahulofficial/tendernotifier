from django.test import LiveServerTestCase
from selenium import webdriver
class Hosttest(LiveServerTestCase):
    def testHomepage(self):
           driver=webdriver.Chrome("chromedriver")
           driver.get("google.com")
