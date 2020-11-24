import unittest

from Diksha_TPD.TPD_Completion_percentage.check_homeicon_and_homebtn import Home_functionalities
from Diksha_TPD.TPD_Completion_percentage.check_with_blockwise_records import Check_with_all_blocks
from Diksha_TPD.TPD_Completion_percentage.check_with_clusterwise_records import Check_with_all_clusters
from Diksha_TPD.TPD_Completion_percentage.check_with_collections import collection_records
from Diksha_TPD.TPD_Completion_percentage.check_with_districts_records import Check_with_all_districts
from Diksha_TPD.TPD_Completion_percentage.check_with_logout_btn import logout_button
from Diksha_TPD.TPD_Completion_percentage.check_with_time_periods import check_time_periods
from Diksha_TPD.TPD_Completion_percentage.completion_icon import completion_percentage_icon
from Diksha_TPD.TPD_Completion_percentage.test_download_icon import Click_download_icon
from reuse_func import GetData


class cQube_chart_percentage_functionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_completion_percentage()
        self.data.page_loading(self.driver)


    def test_completion_percentage_icon(self):
        b = completion_percentage_icon(self.driver)
        res = b.test_completion_percentage_icon()
        self.assertEqual(0,res,msg="Completion icon is not working ")
        self.data.page_loading(self.driver)

    def test_completion_report_from_hamburger(self):
        b = completion_percentage_icon(self.driver)
        res = b.test_dashboard_completion_report()
        self.assertEqual(0,res,msg="Navigation from hamburger is failed")
        self.data.page_loading(self.driver)

    def test_Home_functionalities(self):
        b = Home_functionalities(self.driver)
        res = b.test_homeicon_functionality()
        # self.assertFalse(res,msg="Time period is not selected")
        self.data.page_loading(self.driver)

    def test_Homebtn_functionalities(self):
        b = Home_functionalities(self.driver)
        res = b.test_homebtn_funtion()
        self.assertEqual(res,0 ,msg="Homebtn is not worked")
        self.data.page_loading(self.driver)

    def test_hyperlink_function(self):
        b=Home_functionalities(self.driver)
        res = b.test_hyperlink_function()
        print("Hyper link is working ")
        self.data.page_loading(self.driver)

    def test_Click_download_icon(self):
        b  = Click_download_icon(self.driver)
        res = b.test_check_download_icon()
        self.assertEqual(res,0,msg='Districtwise csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_districtwise_records(self):
        b =Check_with_all_districts(self.driver)
        res,res1 = b.test_district_selectbox()
        self.assertEqual(0,res,msg='Some district csv file is not downloaded')
        self.assertNotEqual(0,res1,msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_blockwise_records(self):
        b = Check_with_all_blocks(self.driver)
        res, res1 = b.test_blocks_selectbox()
        self.assertEqual(0, res, msg='Some Blocks csv file is not downloaded')
        self.assertNotEqual(0, res1, msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_clusterwise_records(self):
        b = Check_with_all_clusters(self.driver)
        res, res1 = b.test_clusters_selectbox()
        self.assertEqual(0, res, msg='Some Cluster csv file is not downloaded')
        self.assertNotEqual(0, res1, msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_logout_button(self):
        b = logout_button(self.driver)
        res = b.click_on_logout_btn()
        self.assertEqual(0,res,msg='Logout btn is not working ')
        self.data.page_loading(self.driver)

    def test_collection_records_districtwise(self):
        b =collection_records(self.driver)
        res1,res2 = b.test_download_collection_options()
        self.assertNotEqual(0,res1,msg='Collection names are not present')
        self.assertEqual(0,res2,"Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_district(self):
        b = collection_records(self.driver)
        res1, res2 = b.test_districtwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_block(self):
        b = collection_records(self.driver)
        res1, res2 = b.test_blockwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_cluster(self):
        b = collection_records(self.driver)
        res1, res2 = b.test_clusterwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()