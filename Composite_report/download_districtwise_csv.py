import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Districtwise_download():
    def __init__(self,driver):
        self.driver = driver
        self.filename =''
    def test_districtwise(self):
        p =pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        self.filename = p.get_download_dir() + "/"+self.fname.composite_district()+management+"_allDistricts_"+self.cal.get_current_date()+'.csv'
        print(self.filename)
        self.cal.page_loading(self.driver)
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)


