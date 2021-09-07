import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class home():
    def __init__(self,driver):
        self.driver = driver
    def test_homeicon(self):
        self.p = GetData()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.driver.find_element_by_id(Data.homeicon).click()

    def test_homebtn(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print("Dashboard Page is displayed ")
        else:
            print('cQube logo is not working ')
            count = count + 1
        self.data.navigate_to_composite_infrastructure()
        self.data.page_loading(self.driver)
        return count

