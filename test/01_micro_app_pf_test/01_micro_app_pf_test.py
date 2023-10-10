from appium_flutter_finder.flutter_finder import  FlutterFinder,FlutterElement
from src.utils.resources import wait_for_visible
from appium import webdriver
import time
import pytest

@pytest.mark.usefixtures("driver_setup")
class TestMicroAppPFOpenAccount:
    finder = FlutterFinder()
    driver: webdriver.Remote = None    
    @pytest.mark.order(1)
    def test_wait_home_app(self):
      
        print('open_app')
        text_finder =  self.finder.by_text('JÁ TENHO CONTA')
        assert wait_for_visible(self.driver,text_finder)
        
    @pytest.mark.order(2)
    def test_open_account(self):
    
        print('open_account')
        text_finder =  self.finder.by_text('ABRA SUA CONTA')
        assert wait_for_visible(self.driver,text_finder)
        time.sleep(2)
        text_element = FlutterElement(self.driver,text_finder)
        text_element.click()
        time.sleep(2)
        
    @pytest.mark.order(3)    
    def test_screen_welcome(self):

        print('screen_welcome')
        text_finder =  self.finder.by_text('CONTINUAR')
        assert wait_for_visible(self.driver,text_finder,timeout=30)
        time.sleep(2)

@pytest.mark.usefixtures("driver_setup")
class TestMicroAppPFLoginAccount:
    finder = FlutterFinder()
    driver: webdriver.Remote = None
    @pytest.mark.order(4)
    def test_open_app(self):
   
        
        print('open_app')
        text_finder =  self.finder.by_text('JÁ TENHO CONTA')
        assert wait_for_visible(self.driver,text_finder)
        
    @pytest.mark.order(5)
    def test_login_account(self):

        print('login_account')
        text_finder =  self.finder.by_text('JÁ TENHO CONTA')
        assert wait_for_visible(self.driver,text_finder)
        time.sleep(2)
        text_element = FlutterElement(self.driver,text_finder)
        text_element.click()
        time.sleep(2)
        