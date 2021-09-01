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
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management_name = self.p.get_management_selected_option()
        self.driver.find_element_by_id(Data.scm_school).click()
        self.p.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(20)
        self.filename = cal.get_download_dir() + '/' +self.fname.scmap_school()+management_name+'_allSchools_'+self.p.get_current_date()+".csv"
        print(self.filename)
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file