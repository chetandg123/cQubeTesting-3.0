import csv
import os
import re
import time
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictCsvDownload():
    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()
    def remove_csv(self):
        os.remove(self.filename)

    def check_districts_csv_download(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        self.year ,self.month = cal.get_student_month_and_year_values()
        cal.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id('period'))
        timeseries.select_by_index(5)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(1, len(select_district.options)-27):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            val = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            distval =val[4:]+'_'
            markers = self.driver.find_elements_by_class_name(Data.dots)
            if len(markers) - 1 == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            time.sleep(2)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() +files.student_districtwise_download()+name+'_blockPerDistricts_of_district_'+distval.strip()+ self.month + "_" + self.year+'_'+cal.get_current_date()+ ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    total = 0
                    schools = 0
                    for row in csv.reader(fin):
                        total += int(row[5])
                        schools += int(row[6])
                    students = self.driver.find_element_by_id("students").text
                    res = re.sub('\D', "", students)

                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)

                    if int(res) != total:
                        print("District" + select_district.first_selected_option.text + "student count mismatched")
                        count = count + 1
                    if int(sc) != schools:
                        print("District" + select_district.first_selected_option.text + "school count mismatched")
                        count = count + 1
                os.remove(self.filename)

        return count

