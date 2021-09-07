
import csv
import os
import time
from selenium.webdriver.support.select import Select
from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

class course_districtwise_lastweek_record():
    def __init__(self,driver):
        self.driver = driver

    def test_each_districts(self):
        self.data = GetData()
        self.msg = file_extention()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index('3')
        self.data.page_loading(self.driver)
        time.sleep(5)
        if self.msg.no_data_found() in self.driver.page_source:
            print(" Last 7 Day's does not have records")
        else:
            districts  =Select(self.driver.find_element_by_id('choose_dist'))
            i = 0
            for x in range(len(districts.options)-3, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                name = districts.options[x].text
                time.sleep(2)
                names = name.strip()
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last 7 days records")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/usage_by_course_content_last_7_days_"+self.data.get_current_date()+".csv"
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    self.data.page_loading(self.driver)
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    tablecount = self.driver.find_elements_by_tag_name('tr')
                    records = int(len(tablecount)) - 2
                    time.sleep(2)
                    # if row_count != records:
                    #     print(districts.options[x].text, row_count,records,"records count mismatch in downloaded file and table records")
                    #     count = count + 1
                    # i = i + 1
        return count