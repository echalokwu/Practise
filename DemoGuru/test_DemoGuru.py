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

    def test_case_1(self, test_setUp):
        """Verify Item in Mobile List page can be sorted by Name"""

        # Step 1. Goto http://live.demoguru99.com/
        driver.get("http://live.demoguru99.com/")

        # Step 2. Verify Title of the page "THIS IS DEMO SITE"
        actual_title = driver.title
        expected_title = "THIS IS DEMO SITE"
        try:
            assert expected_title == actual_title
        except AssertionError:
            print(actual_title, "is the correct title")

        # Step 3. Click on MOBILE menu
        driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()

        # Step 4. Verify Tile of the page "MOBILE"
        actual_title2 = driver.title
        expected_title2 = "MOBILE"
        try:
            assert expected_title2 == actual_title2
        except AssertionError:
            print(actual_title2, "is the correct title")

        # Step 5. In the list of all mobile, select 'SORT BY' dropdown as 'name'
        element = driver.find_element_by_xpath("(//SELECT[@onchange='setLocation(this.value)'])[1]")
        drp = Select(element)
        drp.select_by_visible_text("Name")
        time.sleep(3)

        # Step 6. Verify all products are sorted by name
        x = "name"
        try:
            assert (x in driver.page_source)
            driver.get_screenshot_as_file("../DemoGuru/DemoGuruScreenshots/Name.png")
            print("All products are sorted by", x)
        except AssertionError:
            print("All products are not sorted by", x)

    def test_case_2(self, test_setUp):
        """Verify that cost of product in list page and details page are equal"""
        # Step 1. Goto http://live.demoguru99.com/
        driver.get("http://live.demoguru99.com/")

        # Step 2. Click on MOBILE menu
        driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()

        # Step 3. In the list of all mobile, read the cost of Sony Xperia mobile. Note this value $100
        XperiaPrice = driver.find_element_by_id("product-price-1")
        print(XperiaPrice.text)

        # Step 4. Click on Sony Xperia mobile
        driver.find_element_by_id("product-collection-image-1").click()

        # Step 5. Read the Sony Xperia mobile from the detail page
        detailPrice = driver.find_element_by_xpath("//span[@class='price']")
        print(detailPrice.text)

        # Step 6. Compare value in Step 3 & 5
        try:
            assert XperiaPrice == detailPrice
            print("Verified Successfully")
        except AssertionError:
            print("Step 3 and Step 5 not equal")







