import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class gradewise_records():
    def __init__(self ,driver):
        self.driver = driver

    def grades_files(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for i in range(2, len(grades.options)):
            time.sleep(2)
            grades.select_by_index(i)
            gradename = grades.options[i].text
            gradenum = re.sub('\D', '', gradename).strip()
            self.load.page_loading(self.driver)
            if grades.options[i].text in self.driver.page_source:
                print(grades.options[i].text, 'is displayed in chart ')
                self.load.page_loading(self.driver)
            else:
                print(grades.options[i].text, 'is not displayed ')
                count = count + 1
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.patlo_grades()+management+'_' + gradenum + '_' + 'allDistricts_' + self.month + '_' + self.year + '_' + self.load.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(grades.options[i].text, 'csv file is not downloaded ')
                count = count + 1
            else:
                print(grades.options[i].text, "csv file is downloaded")
            os.remove(self.filename)
        self.load.page_loading(self.driver)
        return count
