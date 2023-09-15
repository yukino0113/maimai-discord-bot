from selenium import webdriver


class DriverBase:
    def __init__(self):
        option = webdriver.EdgeOptions()
        # option.headless = True
        self.driver = webdriver.Edge(option)

    def open_url(self, url):
        self.driver.get(url)

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)
