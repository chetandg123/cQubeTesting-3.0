import os
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class udise_districts_csv():
    def __init__(self,driver):
        self.driver = driver
    def test_districtwise(self):
        self.p = GetData()
        cal = pwd()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allDistricts_'+self.p.get_current_date()+'.csv'
        self.p.page_loading(self.driver)
        print(self.filename)
        file = os.path.isfile(self.filename)
        if True == file:
            print('Udise districtwise csv file is downloaded')
        else:
            print('Districtwise csv file is not downloaded ')
            count = count + 1
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count
