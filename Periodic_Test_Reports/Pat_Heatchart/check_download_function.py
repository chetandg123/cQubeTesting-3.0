import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Download_districtwise():

    def __init__(self,driver):
        self.driver = driver

    def download_all_district_records(self):
        self.p = pwd()
        cal = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(2)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        # self.year,self.month = cal.pat_month_and_year_values()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()

        month = Select(self.driver.find_element_by_id('month'))
        month.select_by_index(1)
        cal.page_loading(self.driver)
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_all_districts()+management+'_all_allDistricts_'+self.month+'_'+self.year+'_'+cal.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
                print("Districtwise csv file is not downloaded")
        else:
             print('District wise csv file is downloaded ')
        os.remove(self.filename)
        cal.page_loading(self.driver)
        return count



