

from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()


    def test_homepageTitle(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.assertEqual('OrangeHRM',self.driver.title,'webpage title is not matching')

    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        self.assertEqual('OrangeHRM',self.driver.title,'webpage title is not matching')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/'
                                                                  'khanb/'
                                                                  'PycharmProjects/'
                                                                  'Project_selenium/'
                                                                  'reports'))