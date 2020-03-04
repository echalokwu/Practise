import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def test_setup():
    """Start web browser"""
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    """Stop we browser"""
    driver.close()
    driver.quit()
    print("Test Completed")


def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    x = driver.title
    assert x == "OrangeHRM"


# def test_teardown():
#     driver.close()
#     driver.quit()
#     print("Test Completed")

