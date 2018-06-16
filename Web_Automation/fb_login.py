from selenium import webdriver
import  time
import sys
sys.path.insert(0,'/home/sudhanshu/Github')
from My_Config import my_email, my_pass

def fb_login():
    browser = webdriver.Firefox()
    browser.get('https://facebook.com')
    time.sleep(40)
    # user credentials
    user = browser.find_element_by_css_selector('#email')
    user.send_keys(my_email)
    password = browser.find_element_by_css_selector('#pass')
    password.send_keys(my_pass)
    login = browser.find_element_by_css_selector('#loginbutton')
    login.click()
    #browser.find_element_by_xpath()

fb_login()