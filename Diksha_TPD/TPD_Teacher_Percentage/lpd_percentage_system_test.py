
import unittest

from Data.parameters import Data
from Diksha_TPD.TPD_Teacher_Percentage.check_blocks_dropdown import Cluster_wise_records
from Diksha_TPD.TPD_Teacher_Percentage.check_clusters_dropdown import School_wise_records
from Diksha_TPD.TPD_Teacher_Percentage.check_district_dropdown import district_level_records
from Diksha_TPD.TPD_Teacher_Percentage.check_with_all_periods import Time_periods

from reuse_func import GetData


class cQube_lpdpercentage_system_Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_percentage_progress()

    def test_navigation_from_hamburger(self):
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('Landing page is displayed ')
        else:
            print('Home btn is not worked')
            count = count + 1
        self.data.navigate_to_tpd_percentage_progress()
        self.data.page_loading(self.driver)
        if 'tpd-teacher-percentage' in self.driver.current_url:
            print('Diksha lpd percentage progress report is present')
        else:
            print('tpd-teacher-percentage report is not displayed')
            count = count + 1
        self.assertEqual(0 ,count ,msg='Navigation failed in landing page')
        self.data.page_loading(self.driver)


    def test_lastday_csv_download(self):
        b = Time_periods(self.driver)
        res = b.check_last_day_districtwise_download()
        self.assertEqual(0 ,res ,msg='Csv file is not downloaded')
        print('Last Day content progress district wise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_last7day_csv_download(self):
        b = Time_periods(self.driver)
        res = b.check_last_7_days_districtwise_download()
        self.assertEqual(0, res, msg='Csv file is not downloaded')
        print('Last 7 Days content progress district wise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_last30day_csv_download(self):
        b = Time_periods(self.driver)
        res = b.check_last_30_day_districtwise_download()
        self.assertEqual(0, res, msg='Csv file is not downloaded')
        print('Last 30 Days content progress district wise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_all_type_csv_download(self):
        b = Time_periods(self.driver)
        res = b.check_all_districtwise_download()
        self.assertEqual(0, res, msg='Csv file is not downloaded')
        print('All time content progress district wise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_all_districts(self):
        b = district_level_records(self.driver)
        res = b.test_all_districtwise()
        self.assertEqual(0 ,res ,msg='All type some district wise csv file not downloaded')
        print('checked with all period all districts')
        self.data.page_loading(self.driver)
    #
    def test_Cluster_wise_records(self):
        b = Cluster_wise_records(self.driver)
        res = b.Blocks_select_box()
        self.assertEqual(0 ,res ,msg="some cluster csv file not downloaded")
        print("checked with cluster wise records")

    def test_School_wise_records(self):
        b = School_wise_records(self.driver)
        res = b.Clusters_select_box()
        self.assertEqual(0 ,res ,msg="School wise csv file is not downloaded")
        print("checked school wise records")
        self.data.page_loading(self.driver)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
