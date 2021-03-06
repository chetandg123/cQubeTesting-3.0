import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class test_crc_report_districtwise():

    def __init__(self,driver):
        self.driver = driver

    def test_districtwise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        self.year , self.month = self.cal.get_crc_month_and_year_values()
        print(self.year,self.month , type(self.year),type(self.month))
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        self.fname=file_extention()
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            value=value.split(":")
            distval= value[1].strip()
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                self.filename = p.get_download_dir() + "/" + self.fname.crc_districtwise()+name+"_"+self.year+"_"+str(self.month)+'_blocks_of_district_'+distval+'_'+self.cal.get_current_date()+'.csv'

                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(select_district.options[x].text,'csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        tschools = 0
                        vsts = 0
                        vstd = 0
                        for row in csv.reader(fin):
                            tschools += int(row[0])
                            vsts +=int(row[2])
                            vstd +=int(row[1])
                        totalschools = self.driver.find_element_by_id("schools").text
                        visited = self.driver.find_element_by_id("visited").text
                        visits = self.driver.find_element_by_id("visits").text
                        tsc = re.sub('\D',"",totalschools)
                        vs = re.sub('\D',"",visits)
                        vd= re.sub('\D', "",visited)
                        if int(tsc) != tschools:
                            print(select_district.options[x].text, ":", "total no of schools  :",tschools, int(tsc),"records are mismatch found")
                        if int(vs) != vsts:
                            print(select_district.options[x].text, ":", "total no of visits  :",int(vs) , vsts,"records are mismatch found")
                        if int(vd) != vstd:
                            print(select_district.options[x].text, ":", "total no of visits  :", int(vd), vstd,
                                  "records are mismatch found")


                    os.remove(self.filename)
        return count