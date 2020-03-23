from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.amazon.com')
        time.sleep(3)

    def like_products(self,product_name):
       
        bot = self.bot
        search_box = bot.find_element_by_id('twotabsearchtextbox')
        search_box.send_keys('iMac')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        for items in range(1,2):
           
            bot.execute_script('window.scrollTo(0,250)')
            time.sleep(2)
            products = bot.find_element_by_class_name('s-image')
            products.click()
            time.sleep(3)
            
            add_cart = bot.find_element_by_id('add-to-cart-button')
            add_cart.click()
            exit()

sarvesh = TwitterBot('yourmail@gmail.com', 'yourpassword')
sarvesh.login()
sarvesh.like_products('iMac')
