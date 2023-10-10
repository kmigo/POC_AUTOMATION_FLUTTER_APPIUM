from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
def wait_for_visible(driver:webdriver.Remote,finder,timeout:int=5):
    
    try:
        driver.execute_script('flutter:waitFor', finder, timeout * 1000)

        return True
    except:
        return False
    
def wait_for_absent(driver:webdriver.Remote,finder,timeout:int=5):
    
    try:
        driver.execute_script('flutter:waitForAbsent', finder, timeout * 1000)

        return True
    except:
        return False
