# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# welc = "Congratulations! You have successfully registered!"
#
#
# def registration(link):
#     with webdriver.Chrome() as browser:
#         browser.implicitly_wait(5)
#         browser.get(link)
#
#         browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]").send_keys("test")
#         browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]").send_keys("test")
#         browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]").send_keys("test")
#
#         browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()
#
#         welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
#         return welcome_text
#
#
# class TestsForPages(unittest.TestCase):
#     def test_first_page(self):
#         p1 = registration("http://suninjuly.github.io/registration1.html")
#         self.assertEqual(p1, welc)
#
#     def test_second_page(self):
#         p2 = registration("http://suninjuly.github.io/registration2.html")
#         self.assertEqual(p2, welc)
#
#
# if __name__ == "__main__":
#     unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

welc = "Congratulations! You have successfully registered!"


def registration(link):
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]").send_keys("test")

        browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text


class TestsForPages(unittest.TestCase):
    def test_first_page(self):
        p1 = registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(p1, welc)

    def test_second_page(self):
        p2 = registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(p2, welc)


if __name__ == "__main__":
    unittest.main()
