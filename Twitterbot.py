from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter_bot():

    #logging in 


    bot = webdriver.Firefox()
    link = 'https://twitter.com/login'
    phonenumber = 'your mobile'
    bot.get(link)
    time.sleep(3)
    username  =  bot.find_element_by_name('session[username_or_email]')
    username.clear()
    username.send_keys(phonenumber)
    time.sleep(3)
    password = bot.find_element_by_name('session[password]')
    password.clear()
    password.send_keys("yourpassword")
    password.send_keys(Keys.RETURN)
    time.sleep(4)


    #searching


    search_twitter = bot.find_element_by_class_name('r-30o5oe')
    search_twitter.clear()
    search_twitter.click()
    search_twitter.send_keys('anytopic')
    search_twitter.send_keys(Keys.RETURN)
    time.sleep(3)
    bot.execute_script('window.scrollTo(0,500)')
    time.sleep(3)
    bot.execute_script('window.scrollTo(0,500)')
    time.sleep(3)

    #going back to home
    home_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div')
    home_button.click()


    #sending tweets

    time.sleep(2)
    tweet = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
    tweet.click()
    time.sleep(3)
    message = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
    message.click()
    time.sleep(3)
    message.send_keys('Hi')
    time.sleep(2)
    submit = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')
    submit.click()
    time.sleep(3)
    bot.execute_script('window.history.back(-1)')
    

    bot.quit()