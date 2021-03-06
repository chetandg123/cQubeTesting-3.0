import os
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class click_schoolbutton():
    def __init__(self,driver):
        self.driver =driver

    def test_click_on_school_btn(self):
        self.p = GetData()
        cal = pwd()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_school).click()
        time.sleep(30)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allSchools_'+self.p.get_current_date() +'.csv'
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file