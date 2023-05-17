from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG= '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    # file = open('../config/kyb_caps.yaml','r')
    # data = yaml.load(file)
    # file.close()
    with open('../config/kyb_caps.yaml','r',encoding='utf-8') as File:
        data = yaml.load(File)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_dir)
    app_path = os.path.join(base_dir, 'app', data['appName'])
    # print(app_path)
    desired_caps['app']=app_path
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('----start app----')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)
    return driver

if __name__ =='__main__':
    appium_desired()

