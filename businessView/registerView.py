import logging,random
import time

from common.desried_caps import appium_desired
from common.common_fun import Common,By,NoSuchElementException

class RegisterView(Common):
    register_text=(By.ID,'com.tal.kaoyan:id/login_register_text')
    #头像设置相关元素
    register_userheader=(By.ID,'com.tal.kaoyan:id/activity_register_userheader')
    item_image=(By.ID,'com.tal.kaoyan:id/item_image')
    save=(By.ID,'com.tal.kaoyan:id/save')

    #用户名、密码、邮箱相关元素
    register_username=(By.ID,'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password=(By.ID,'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email=(By.ID,'com.tal.kaoyan:id/activity_register_email_edittext')

    register_btn=(By.ID,'com.tal.kaoyan:id/activity_register_register_btn')

    #完善资料界面元素
    title=(By.ID,'com.tal.kaoyan:id/myapptitle_Title')
    time=(By.ID,'com.tal.kaoyan: id / activity_perfectinfomation_time')
    school_name=(By.ID,'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    major=(By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major')
    goBtn=(By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    #院校相关元素
    forum_title=(By.ID,'com.tal.kaoyan:id/more_forum_title')
    university=(By.ID,'com.tal.kaoyan:id/university_search_item_name')

    #专业相关元素
    major_subject_title=(By.ID,'com.tal.kaoyan:id/major_subject_title')
    major_group_title=(By.ID,'com.tal.kaoyan:id/major_group_title')
    major_search_item_name=(By.ID,'com.tal.kaoyan:id/major_search_item_name')

    #用户中心相关元素
    button_myself=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self,register_username,register_password,register_email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('----register_action----')
        self.driver.find_element(*self.register_text).click()

        logging.info('----set userimage----')
        self.driver.find_element(*self.register_userheader).click()
        self.driver.find_elements(*self.item_image)[4].click()
        self.driver.find_element(*self.save).click()
        time.sleep(4)

        logging.info('----username is %s----'%register_username)
        self.driver.find_element(*self.register_username).send_keys(register_username)
        logging.info('----password is %s----'%register_password)
        password=self.driver.find_element(*self.register_password)
        password.click()
        password.send_keys(register_password)
        logging.info('----email is %s----'%register_email)
        email=self.driver.find_element(*self.register_email)
        email.click()
        email.send_keys(register_email)

        logging.info('----register_btn----')
        self.driver.find_element(*self.register_btn).click()

        time.sleep(15)
        try:
            logging.info('----check_element----')
            self.driver.find_element(*self.title)
            # self.driver.find_element(*self.school_name)
        except NoSuchElementException:
            logging.error('----register fail !----')
            self.getScreenshot('register fail')
            return False
        else:
            self.add_register_info()
            if self.check_register_station():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('----add_register_info----')

        logging.info('----select school----')
        self.driver.find_element(*self.school_name).click()
        self.find_elements(*self.forum_title)[1].click()
        self.find_elements(*self.university)[1].click()

        logging.info('----select major----')
        self.driver.find_element(*self.major).click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_group_title)[2].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()

        self.driver.find_element(*self.goBtn).click()

    def check_register_station(self):
        logging.info('----check_register_station----')
        self.check_market_ad()
        try:
            time.sleep(3)
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.info('----register fail!----')
            self.getScreenshot('register fail')
            return False
        else:
            logging.info('----register success!----')
            return True
if __name__=='__main__':
    driver=appium_desired()
    register=RegisterView(driver)

    username = 'mm5024' + str(random.randint(888,9999))
    password = 'm2y0m' + str(random.randint(888,9999))
    email = '2mn2' + str(random.randint(888,9999)) + '@qq.com'
    register.register_action(username,password,email)











