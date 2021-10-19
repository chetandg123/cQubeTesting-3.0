import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictBlockCluster():
    def __init__(self, driver):
        self.driver = driver
    def remove_csv(self):
        os.remove(self.filename)

    def check_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(3)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value[3:]
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename = p.get_download_dir() +"/" + self.fname.sr_clusterwise()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__schools_of_cluster_'+value.strip()+'_'+cal.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + " Block: " + select_block.first_selected_option.text + " Cluster: " + select_cluster.first_selected_option.text + "csv is not downloaded")
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

    def check_last30_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        time.sleep(3)
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text ,' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            count = 0
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(1, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_clusterwise() + management+'_'+timeseries+ '_allGrades__schools_of_cluster_' + values+ cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
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

    def check_last7_district_block_cluster(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        time.sleep(3)
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
            return count
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' +values+ cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
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