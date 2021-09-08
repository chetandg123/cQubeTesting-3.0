import time
import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.parameters import Data
from Student_Attendance.Click_on_hyper_link_in_SAR import Hyperlink
from Student_Attendance.check_data_range import DateRange
from Student_Attendance.check_with_total_schools_in_SAR import TotalSchools
from Student_Attendance.check_with_total_student_in_SAR import TotalStudents
from Student_Attendance.click_on_Home_icon import Home
from Student_Attendance.click_on_SAR import DahboardSar
from reuse_func import GetData


class cQube_Student_Attendance(unittest.TestCase):

    data = None
    driver = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_student_report()
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text


    def test_click_on_student_attendence_report(self):
        sar = DahboardSar(self.driver)
        result = sar.click_on_sar()
        if "student-attendance" in result:
            print("Student Attendance Infra_Table_Report is Working")
        else:
            raise self.failureException("Student Attendance Infra_Table_Report Is Not Working")

    def test_click_on_blocks(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Blocks_btn))
        )
        try:
            element.click()
            time.sleep(5)
            print("Blocks Button is working")
        except WebDriverException:
            raise self.failureException("Blocks Button is not clickable")

    def test_click_on_clusters(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Clusters_btn))
        )
        try:
            element.click()
            self.data.page_loading(self.driver)
            print("Cluster Button is working")
        except WebDriverException:
            raise self.failureException("Cluster Button is not working")

    def test_click_on_schools(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Schools_btn))
        )
        try:
            element.click()
            self.data.page_loading(self.driver)
            print("Schools Button is working")
        except WebDriverException:
            raise self.failureException("Schools Button is not working")

    def test_logout(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        self.assertEqual("Log in to cQube", self.driver.title,msg="Logout is not worked")
        time.sleep(2)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        print("Logout functionality is working fine...")
        self.data.page_loading(self.driver)


    def test_check_hyperlinks(self):
        hyperlinks = Hyperlink(self.driver)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        # if result1 == False and result2 == False and choose_dist == "Choose a District ":
        #     print("hyperlinks are working")
        # else:
        #     raise self.failureException("hyperlinks are not working")
    #
    # def test_select_year(self):
    #     state = GetData()
    #     state.click_on_state(self.driver)
    #     year = Select(self.driver.find_element_by_id(Data.sar_year))
    #     try:
    #         for x in range(1, len(year.options)):
    #             year.select_by_index(x)
    #             self.data.page_loading(self.driver)
    #         print("Select year is working")
    #     except WebDriverException:
    #         raise self.failureException("Select Year is not working")

    # def test_select_month(self):
    #     state = GetData()
    #     state.click_on_state(self.driver)
    #     year = self.driver.find_element_by_id(Data.sar_year)
    #     month = Select(self.driver.find_element_by_id(Data.sar_month))
    #     try:
    #         for x in range(1, len(month.options)):
    #             month.select_by_index(x)
    #             self.data.page_loading(self.driver)
    #         print("Select month is working")
    #     except WebDriverException:
    #         raise self.failureException("Select month is not working")

    def test_choose_district_block_cluster(self):
        dist = DistrictCsvDownload(self.driver, self.year, self.month)
        result = dist.check_districts_csv_download()
        if result == 0:
            print("Block per district csv report download is working")
            print("on selection of each district")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Block per district csv report download is working")
        block = ClusterPerBlockCsvDownload(self.driver, self.year, self.month)
        result = block.check_csv_download()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Cluster per block csv report download is working")
        schools = DistrictBlockCluster(self.driver, self.year, self.month)
        result = schools.check_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download is working")

    def test_home_icon(self):
        home = Home(self.driver)
        home.click_on_blocks_click_on_home_icon()
        result = home.click_HomeButton()
        if "student-attendance" in result:
            print("Home Icon is Working")
        else:
            raise self.failureException('Home Icon is not working')

    def test_download(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = self.driver.find_element_by_id(Data.Download)
        try:
            element.click()
            time.sleep(3)
            print("Download Button is working")
        except WebDriverException:
            raise self.failureException("Download Button is not working")

    def test_markers_on_map(self):
        state = GetData()
        state.click_on_state(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        if int(len(dots) - 1) != 0:
            print('Markers are present on the map')
        else:
            raise self.failureException("Markers are not present on the map")

    def test_no_of_schools_is_equals_at_districts_blocks_clusters_schools(self):
        tc = TotalSchools(self.driver)
        schools, Bschools = tc.block_no_of_schools()
        self.assertEqual(int(schools), int(Bschools), msg="Block level no of schools are not equal to no of schools ")
        schools, Cschools = tc.cluster_no_of_schools()
        self.assertEqual(int(schools), int(Cschools), msg="Cluster level no of schools are not equal to no of schools ")
        schools, Sschools = tc.schools_no_of_schools()
        self.assertEqual(int(schools), int(Sschools), msg="Cluster level no of schools are not equal to no of schools ")

    def test_total_no_of_students_is_equals_at_districts_blocks_clusters_schools(self):
        tc = TotalStudents(self.driver)
        student_count, Bstudents = tc.block_total_no_of_students()
        self.assertEqual(int(student_count), int(Bstudents), msg="Block level no of students are not equal")
        student_count, Cstudents = tc.cluster_total_no_of_students()
        self.assertEqual(int(student_count), int(Cstudents), msg="Cluster level no of students are not equal")
        student_count, Sstudents = tc.schools_total_no_of_students()
        self.assertEqual(int(student_count), int(Sstudents), msg="Cluster level no of students are not equal")
    #
    # def test_date_range(self):
    #     daterange = DateRange(self.driver)
    #     result = daterange.check_date_range()
    #     self.driver.find_element_by_id(Data.menu_icon).click()
    #     time.sleep(2)
    #     self.data.navigate_to_student_report()
    #     self.data.page_loading(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
