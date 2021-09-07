from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class Home_functions():
    def __init__(self,driver):
        self.driver = driver

    def test_homeicons(self):
        self.load =GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id(Data.exam_dates))
        timeseries.select_by_index(2)
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.load.page_loading(self.driver)

    def test_homebutton(self):
        self.load = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_lo_table_report()
        self.load.page_loading(self.driver)
        if 'PAT-LO-table' in self.driver.current_url:
            print('Pat LO Table is present ')
        else:
            print('Home button is not working ')
            count = count + 1
        self.load.page_loading(self.driver)
        return count