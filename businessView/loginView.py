import logging
import time

from selenium.webdriver.common.by import By
from common.common_fun import Common
from common.desried_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException

class loginView(Common):
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    tip_commit=(By.ID,'com.tal.kaoyan:id/tip_commit')

    myselfBtn=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    RightButton=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logout=(By.ID,'com.tal.kaoyan:id/setting_logout_text')


    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('----login_action----')
        logging.info('----username is :%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('----password is:%s' %password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('----click loginBtn----')
        self.driver.find_element(*self.loginBtn).click()

        logging.info('----login finished----')

    def check_account_alert(self):
        logging.info('----check_account_alert----')
        try:
            time.sleep(5)
            element=self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            logging.info('----no tip_commit----')
        else:
            logging.info('----close tip_commint----')
            element.click()

    def check_login_status(self):
        logging.info('----check_login_status----')
        self.check_market_ad()
        self.check_account_alert()
        time.sleep(2)
        try:
            self.driver.find_element(*self.myselfBtn).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('----login Fail----')
            self.getScreenshot('loginFail')
        else:
            logging.info('----login sussess----')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('----check_logout_action----')
        try:
            self.driver.find_element(*self.RightButton).click()
            self.driver.find_element(*self.logout).click()
            self.driver.find_element(*self.tip_commit).click()

        except NoSuchElementException:
            logging.error('----logout Fail----')
            self.getScreenshot('logoutFail')
        else:
            logging.info('----logout success----')
            return True



if __name__=='__main__':
    driver=appium_desired()
    driver.implicitly_wait(5)
    l=loginView(driver)
    l.login_action('自学网2018','zxw2018')
    l.check_login_status()
