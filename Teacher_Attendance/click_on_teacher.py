import time

from selenium.common.exceptions import ElementClickInterceptedException

from Data.parameters import Data
from reuse_func import GetData


class DahboardSar():
    def __init__(self, driver):
        self.driver = driver

    def click_on_tar(self):
        try:
            cal = GetData()
            cal.click_on_state(self.driver)
            cal.page_loading(self.driver)
            self.driver.find_element_id(Data.cQube_logo).click()
            time.sleep(1)
            cal.navigate_to_teacher_attendance_report()
            cal.page_loading(self.driver)
            return self.driver.current_url

        except ElementClickInterceptedException:
            print("Element not found and test failed")



