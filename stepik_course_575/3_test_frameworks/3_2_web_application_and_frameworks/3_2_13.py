import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def test_browser(link):
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

        return browser.find_element(By.TAG_NAME, "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(test_browser("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(test_browser("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()
