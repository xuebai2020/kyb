from selenium.webdriver.common.by import By
from baseView.baseView import BaseView
from common.desried_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
import time,os
import csv

class Common(BaseView):
    cancelBtn= (By.ID,'android:id/button2')
    skipBtn= (By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel= (By.ID,"com.tal.kaoyan:id/view_wemedia_cacel")

    def check_cancelBtn(self):
        logging.info('------check_cancelBtn------')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('------check_skipBtn-------')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('------no skipBtn------')
        else:
            skipBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1,y1,x2,y1,1000)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        y2 = int(l[1] * 0.1)
        self.swipe(x1,y1,x1,y2,1000)

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenshot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('------get %s screenshot------' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('------check_market_ad------')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            logging.info('---no wemedia_cacel---')
        else:
            logging.info('---close market_ad---')
            element.click()

    def get_csv_data(self,csv_file,line):
        logging.info('----get_csv_data----')
        with open(self.csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index,data in enumerate(reader,1):
                if index==line:
                    return index,data

if __name__ == '__main__':
    '''
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    #com.check_skipBtn()
    # com.get_size()
    time.sleep(2)
    com.swipeLeft()
    time.sleep(2)
    com.swipeLeft()
    time.sleep(2)
    com.getScreenshot('startapp')
    '''


    '''
    csv_file='../data/data.csv'
    data=get_csv_data(csv_file,2)
    print(data)
    print('行号：%s' %data[0])
    print('用户名：%s' %data[1][0])
    print('密码：%s' %data[1][1])
    '''