from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")

        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
            # element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
            print("element is clickable")
            element.click()

        except TimeoutException:
            print("element is not clickable")
            exit(2)


if __name__ == '__main__':
    unittest.main()
