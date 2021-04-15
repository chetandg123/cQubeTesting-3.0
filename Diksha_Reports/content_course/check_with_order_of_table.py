import time

from Data.parameters import Data
from reuse_func import GetData


class Table_orderwise():
    def __init__(self,driver):
        self.driver = driver

    def test_tablevalue(self):
        self.p = GetData()
        time.sleep(4)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='table_wrapper']/div/div[1]/div/table/thead/tr/th[1]").click()
        self.p.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[2]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='table_wrapper']/div/div[1]/div/table/thead/tr/th[1]").click()
        self.p.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[2]")
        for i in value:
            print(i.get_attribute("aria-sort"))
        self.p.page_loading(self.driver)




