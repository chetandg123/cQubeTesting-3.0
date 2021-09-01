import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class download_blockwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_blockwise(self):
        p =pwd()
        self.cal  = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id('allBlock').click()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_block()+management+'_allBlocks_'+self.cal.get_current_date()+'.csv'
        time.sleep(3)
        print(self.filename)
        return os.path.isfile(self.filename)
    def remove_file(self):
        os.remove(self.filename)

