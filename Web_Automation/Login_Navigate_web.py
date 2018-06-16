from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
import unittest
import pickle #for my personal email Database

# For Importing my credentials
import sys
sys.path.insert(0,'/home/sudhanshu/Github')
from My_Config import my_email, my_pass

# Invitaion batch size
__BATCH_SIZE = 900

class ClearTax(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://cleartax.in/Account/LogOn?ref=login-modal')

    def login(self):
        emailFieldId='UserName'
        passFieldId = 'Password'
        loginButtonXpath = '//button[contains(@value,"Log On")]'

        emailFieldElement = WebDriverWait(self.driver, 10).until(lambda  driver: driver.find_element_by_id(emailFieldId))
        passFieldElement = WebDriverWait(self.driver,10).until(lambda driver : driver.find_element_by_id(passFieldId))
        loginButtonElement = WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(my_email)
        passFieldElement.clear()
        passFieldElement.send_keys(my_pass)
        loginButtonElement.click()

    def go_to_Refer(self):
        self.login()
        referButtonXpath = '(//a[contains(@href,"/ReferralCampaign")])[3]'

        referButtonElement = WebDriverWait(self.driver,10).until(lambda  driver: driver.find_element_by_xpath(referButtonXpath))
        referButtonElement.click()

    def invite(self,mails=['test1@gmail.com','test2@gmail.com']):
        mailsXpath='//input[contains(@placeholder,"Type multiple email IDs")]'
        inviteButtonXpath = '//span[contains(@class,"input-group-addon")]'
        closePopXpath = '//button[contains(@class,"close referral-invite")]'

        mail_element = WebDriverWait(self.driver, 10).until(lambda driver : driver.find_element_by_xpath(mailsXpath))

        for mail in mails:
            mail_element.send_keys(mail)
            mail_element.send_keys(',')

        inviteButtonElement = WebDriverWait(self.driver, 10).until(lambda driver : driver.find_element_by_xpath(inviteButtonXpath))
        inviteButtonElement.click()
        try:
            close_popup = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(closePopXpath))
            close_popup.click()
        except:
            input('Waiting for admin as error Happend :( ')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    obj = ClearTax()
    obj.setUp()
    obj.go_to_Refer()


    # Fetching emails and paste __BATCH_SIZE at a time
    with open('/home/sudhanshu/Github/G_Emials.pkl', 'rb') as db:
        emails = pickle.load(db)
    print('Total emails at begining : ', len(emails))

    try:
        while len(emails) >0:
            print('\nCurrent status of emails', len(emails),'\n')
            if len(emails) >__BATCH_SIZE:
                obj.invite(emails[:__BATCH_SIZE])
                emails = emails[__BATCH_SIZE+1:]
            else:
                obj.invite(emails)
                emails = []

    except:
        print('Oh Crap Error Happen')
        print('Closing mails statics :', len(emails))
        with open('/home/sudhanshu/Github/G_Emials.pkl', 'wb') as db:
            pickle.dump(emails, db)
        exit(-1)

    print('Closing mails statics :', len(emails))
    with open('/home/sudhanshu/Github/G_Emials.pkl', 'wb') as db:
        pickle.dump(emails, db)