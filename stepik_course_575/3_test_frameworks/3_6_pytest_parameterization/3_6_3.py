from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

lessons = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
text = ""


def answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("lesson", lessons)
def test_find_hidden_text(browser, lesson):
    global text
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)

    browser.find_element(By.CLASS_NAME, "ember-text-area")
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer())
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    check_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert check_text == "Correct!", f"got {check_text}, but should be 'Correct!'"
    # try:
    #     assert "Correct" in check_text
    # except:
    #     with open("3_6_3_test_Errors.log", "a") as f:
    #         f.write(check_text)
    #     raise AssertionError("Error! See 3_6_3_test_Errors.log")
