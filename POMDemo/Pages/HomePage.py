from POMDemo.Locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText
        self.admin = driver.find_element_by_xpath(Locators.admin)
        self.job = driver.find_element_by_id(Locators.job)
        self.job_title = driver.find_element_by_xpath(Locators.job_title)

    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(Locators.logout_link_linkText).click()











