import csv
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class SchoolInfra_scores():
    
    
    def __init__(self,driver):
        self.driver = driver
        
    def infra_score(self):
        self.fname = file_extention()
        self.cal = GetData()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        management_name = self.cal.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Infra score percentage is selected and csv file is downloaded")
        return row_count-1


    def Boys_toilet_percentage(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.cal.page_loading(self.driver)
        management_name = self.cal.get_management_selected_option()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Boy's toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def drinking_water(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Drinking water percentage is selected and csv file is downloaded")
        return row_count-1

    def Electricity(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Electricity percentage is selected and csv file is downloaded")
        return row_count-1

    def girls_toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("girls toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def Handpump(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Hand pump percentage is selected and csv file is downloaded")
        return row_count-1

    def Handwash(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Handwash percentage is selected and csv file is downloaded")
        return row_count-1

    def Library(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Library percentage is selected and csv file is downloaded")
        return row_count-1

    def Solar_panel(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("solar panel percentage is selected and csv file is downloaded")
        return row_count-1

    def Tapwater(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Tapwater percentage is selected and csv file is downloaded")
        return row_count-1

    def Toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def infra_score_dropdown(self):
        self.fname = file_extention()
        self.cal = GetData()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        infraoptions = Select(self.driver.find_element_by_id('choose_infra'))
        for i in range(1,len(infraoptions.options)):
            infraoptions.select_by_index(i)
            self.cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.management_name = self.cal.get_management_selected_option()
            filename = p.get_download_dir() + "/" + self.fname.scmap_district()+self.management_name+'_allDistricts_'+self.cal.get_current_date()+'.csv'
            row_count = 0
            with open(self.filename, 'rt')as f:
                reader = csv.reader(f)
                data = list(reader)
                row = len(data)
                row_count = row
            print(infraoptions.options[i].text,"is selected and csv file is downloaded")
            os.remove(self.filename)
            return row_count - 1


    def remove_csv(self):
        os.remove(self.filename)
