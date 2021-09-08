import csv
import os
import re
import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

import pandas as pd
class DistrictwiseDownload():
    def __init__(self, driver):
        self.driver = driver
        self.filename =''

    def check_districts_csv_download(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value[4:]+'_'
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/" + self.fname.exception_districtwise()+management+'_overall_allGrades__blocks_of_district_'+value.strip()+cal.get_current_date()+'.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            else:
                # with open(self.filename) as fin:
                #     csv_reader = csv.reader(fin, delimiter=',')
                #     header = next(csv_reader)
                #     schools = 0
                #     for row in csv.reader(fin):
                #         schools += int(row[6].replace(',', ''))
                data = pd.read_csv(self.filename)
                schools = data['Total Schools With Missing Data'].sum()
                missingdata = self.driver.find_element_by_id('schools').text
                md = re.sub('\D', '', missingdata)
                if int(schools) != int(md):
                    print("District" + select_district.first_selected_option.text, schools, md)
                    count = count + 1
                os.remove(self.filename)
            return count








