from selenium import webdriver
import unittest
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/echalo/Desktop/AutomationTesting/Practise'])
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.Pages.HomePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage
import time
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver = webdriver.Chrome(
        # executable_path="/Users/echalo/Desktop/AutomationTesting/Practise/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(2)

    def test_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin")
        login.click_login()
        time.sleep(2)

        # homepage = HomePage(driver)
        # actions = ActionChains(driver)
        # actions.move_to_element(homepage.admin)
        # actions.move_to_element(homepage.job)
        # actions.click(homepage.job_title)
        # actions.perform()
        # homepage.click_welcome()
        # homepage.click_logout()
        # time.sleep(2)


if __name__ == '__main__':
    unittest.main()
