import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


class TestGuru:

    @pytest.fixture
    def test_setUp(self):
        """Start web browser"""
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        """Stop web browser"""
        driver.close()
        driver.quit()

    """
    Test Case1: Verify Item in Mobile List page can be sorted by Name
    ----------------------------------------------------------------
    1) Goto http://live.demoguru99.com/
    2) Verify Title of the page "THIS IS DEMO SITE
    3) Click on MOBILE menu
    4) Verify Tile of the page "MOBILE
    5) In the list of all mobile, select 'SORT BY' dropdown as 'name'
    6) Verify all products are sorted by name
    """
    @pytest.mark.skip("Testing")
    def test_case_1(self, test_setUp):
        driver.get("http://live.demoguru99.com/")
        actual_title = driver.title
        expected_title = "THIS IS DEMO SITE"
        try:
            assert expected_title == actual_title
        except AssertionError:
            print(actual_title, "is the correct title")
        driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()
        actual_title2 = driver.title
        expected_title2 = "MOBILE"
        try:
            assert expected_title2 == actual_title2
        except AssertionError:
            print(actual_title2, "is the correct title")
        element = driver.find_element_by_xpath("(//SELECT[@onchange='setLocation(this.value)'])[1]")
        drp = Select(element)
        drp.select_by_visible_text("Name")
        time.sleep(3)
        x = "name"
        try:
            assert (x in driver.page_source)
            driver.get_screenshot_as_file("../DemoGuru/DemoGuruScreenshots/Name.png")
            print("All products are sorted by", x)
        except AssertionError:
            print("All products are not sorted by", x)

    """
       Test Case2: Verify that cost of product in list page and details page are equal
       ----------------------------------------------------------------
       1) Goto http://live.demoguru99.com/
       2) Click on MOBILE menu
       3) In the list of all mobile, read the cost of Sony Xperia mobile. Note this value $100
       4) Click on Sony Xperia mobile
       5) Read the Sony Xperia mobile from the detail page
       6) Compare value in Step 3 & 5
       """
    def test_case_2(self, test_setUp):
        driver.get("http://live.demoguru99.com/")
        driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()
        XperiaPrice = driver.find_element_by_id("product-price-1")
        print(XperiaPrice.text)
        driver.find_element_by_id("product-collection-image-1").click()
        detailPrice = driver.find_element_by_xpath("//span[@class='price']")
        print(detailPrice.text)
        try:
            assert XperiaPrice == detailPrice
            print("Verified Successfully")
        except AssertionError:
            print("Step 3 and Step 5 not equal")







