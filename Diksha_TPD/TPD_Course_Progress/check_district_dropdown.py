import csv
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class district_level_records():
    def __init__(self, driver):
        self.driver = driver

    def test_all_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Overall ')
        period.select_by_index(1)
        print(period.first_selected_option)
        self.load.page_loading(self.driver)
        for i in range(1, len(dists.options)):
            dists.select_by_index(i)
            time.sleep(2)
            value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
            value = value[3:]+'_'
            self.load.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            self.filename = self.p.get_download_dir() +"/" + self.fname.tpd_all_districtwise()+value.strip()+self.load.get_current_date()+'.csv'
            print(self.filename)
            file = os.path.isfile(self.filename)
            if file != True:
                print(dists.options[i].text, 'District wise records csv file is not downloaded')
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                os.remove(self.filename)
                time.sleep(2)
                if row_count == 0:
                    print("records are not found in csv file ")
                    count = count + 1
            return count

        return count

    def test_last_day_districtwise(self):
        self.driver.implicitly_wait(100)
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last Day ')
        period.select_by_index(4)
        self.load.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:
            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value[4:] + '_'
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() +"/" + self.fname.tpd_lastday_districtwise()+value.strip()+self.load.get_current_date()+'.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
        return count

    def test_last_7_days_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        self.driver.implicitly_wait(100)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.load.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:

            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value[4:] + '_'
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() +"/"+ self.fname.tpd_lastweek_districtwise()+value.strip()+self.load.get_current_date()+'.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
        return count

    def test_last_30_days_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.driver.implicitly_wait(50)
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last 30 Days ')
        period.select_by_index(2)
        self.load.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:
            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value[4:] + '_'
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() +"/"+self.fname.tpd_lastmonth_districtwise()+value.strip()+self.load.get_current_date()+'.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
                    self.load.page_loading(self.driver)
        return count