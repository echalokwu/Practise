import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestOurSky:

    @pytest.fixture()
    def test_setUp(self):
        """Start web driver"""
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        yield
        """Stop web driver"""
        driver.close()
        driver.quit()

    def test_case_1(self, test_setUp):
        """Find and click top-right button"""
        driver.get('https://www.oursky.com/')
        driver.find_element_by_class_name('btn-header').click()
        expected = ('Oursky - Web & mobile application development company based in Hong Kong')
        assert driver.title == expected
        print(driver.title)

    def test_case_2(self, test_setUp):
        """Find and click Learn more button"""
        driver.get('https://www.oursky.com/')
        driver.find_element_by_xpath(".//*[@id='tag-line-wrap']/span/a").click()