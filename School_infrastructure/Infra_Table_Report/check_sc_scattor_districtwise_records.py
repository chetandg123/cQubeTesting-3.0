import csv
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class test_districtwise():

    def __init__(self,driver):
        self.driver = driver

    def test_districtwise(self):
        p = pwd()
        self.cal = GetData()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(len(select_district.options)-4, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute("value")
            blkval =value.split(":")
            val = blkval[1].strip()
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = p.get_download_dir() + "/" + self.fname.sc_districtwise()+management+'_blocks_of_district_'+(val+'_').strip()+self.cal.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print(select_district.options[x].text , " csv file is not downloaded")
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_dict = [row for row in csv.DictReader(self.filename)]
                        if len(csv_dict) == 0:
                            print(select_district.options[x].text,'csv file is empty')
                    os.remove(self.filename)

        return count