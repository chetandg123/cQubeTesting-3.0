import csv
import os
import re
import time

from selenium.webdriver.support.select import Select


from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictsBlock():
    def __init__(self, driver):
        self.driver = driver

    def remove_csv(self):
        os.remove(self.filename)

    def check_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-2, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value[4:]+'_'
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text +"No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__clusters_of_block_'+value.strip()+cal.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text +"Block "+ select_block.first_selected_option.text+"csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        self.remove_csv()

                return count

    def check_last30days_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period =Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ",'_')
        time.sleep(3)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise()+management+'_'+timeseries+'_allGrades__clusters_of_block_' + values+'_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        self.remove_csv()

                return count

    def check_last7days_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        count = 0
        if 'No data found' in self.driver.page_source:
            print(timeseries,'is not having Data..')
            return count
        else:
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options)-3, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                    value = value.split(":")
                    values = value[1].strip()
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                        count = count + 1
                    else:
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(4)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise() + management +"_"+timeseries + '_allGrades__clusters_of_block_' + values+"_"+ cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                data = list(csv_reader)
                                row_count = len(data)
                                dots = len(markers) - 1
                                if dots != row_count:
                                    print('Markers records and csv file records are not matching ', dots, row_count)
                                    count = count + 1
                            self.remove_csv()
                    return count