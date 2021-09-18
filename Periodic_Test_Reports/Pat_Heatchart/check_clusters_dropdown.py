import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Clusterswise():
    def __init__(self, driver):
        self.driver = driver

    def check_block_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.year , self.month = self.load.get_pat_month_and_year_values()
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D','',gradename).strip()
            self.load.page_loading(self.driver)
            for i in range(len(dists.options)-1, len(dists.options)):
                dists.select_by_index(i)
                self.load.page_loading(self.driver)
                for j in range(len(Blocks.options)-1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.load.page_loading(self.driver)
                    value = self.driver.find_element_by_id(Data.blocks_dropdown).get_attribute('value')
                    bvalue = value.split(":")
                    val = bvalue[1].strip()
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_clusters() + management + '_' + gradenum + "_clusters_of_block_"+val+'_'+ self.month + '_' + self.year + '_' + \
                                    self.load.get_current_date() + '.csv'
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    if file != True:
                        print(Blocks.options[j].text, 'Block wise records csv file is not downloaded')
                        count = count + 1
                    self.load.page_loading(self.driver)
                    os.remove(self.filename)
                return count


    def Clusters_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.year , self.month = self.load.get_pat_month_and_year_values()
        clust = Select(self.driver.find_element_by_id(Data.cluster_dropdown))
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D','',gradename).strip()
            self.load.page_loading(self.driver)
            for i in range(len(dists.options)-1, len(dists.options)):
                dists.select_by_index(i)
                self.load.page_loading(self.driver)
                for j in range(len(Blocks.options)-1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.load.page_loading(self.driver)
                    for k in range(1, len(clust.options)):
                        clust.select_by_index(k)
                        self.load.page_loading(self.driver)
                        if 'No data found' in self.driver.page_source:
                            print("No data available ")
                        else:
                            value =self.driver.find_element_by_id(Data.cluster_dropdown).get_attribute('value')
                            value = value[3:]+'_'
                            print(value)
                            self.driver.find_element_by_id(Data.Download).click()
                            time.sleep(3)
                            self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_schools()+management+'_'+gradenum+"_schools_of_cluster_"+value.strip()+self.month+'_'+self.year+'_'+ \
                            self.load.get_current_date()+'.csv'
                            print(self.filename)
                            file = os.path.isfile(self.filename)
                            if file != True:
                                print(clust.options[k].text, 'Cluster wise records csv file is not downloaded')
                                count = count + 1
                            self.load.page_loading(self.driver)
                            os.remove(self.filename)
                            return count