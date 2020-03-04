import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_search1(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Google Search")
        time.sleep(2)

    def test_search2(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav pal")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Raghav pal - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/echalo/Desktop/AutomationTesting/Practise/reports'), verbosity=2)
