import os
import time
from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Download_districtwise():
    def __init__(self,driver):
        self.driver = driver

    def download_all_district_records(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_id(Data.home).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_lo_table_report()
        self.load.page_loading(self.driver)
        self.year,self.month = self.load.get_pat_month_and_year_values()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_all_districts()+management+'_overall_allDistricts_'+self.month+'_'+self.year+'_'+self.load.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Districtwise csv file is not downloaded ')
            count = count + 1
        else:
            print('District wise csv file is downloaded ')
        self.load.page_loading(self.driver)
        os.remove(self.filename)
        return count



