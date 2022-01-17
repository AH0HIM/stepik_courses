import time

import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

scriptDirectory = pathlib.Path().absolute()
chrome_option = Options()
chrome_option.add_argument(f"--user-data-dir={scriptDirectory}\\userdata")
driver = webdriver.Chrome(options=chrome_option)

chrome_option.add_argument("--user-data-dir=chrome-data")
driver.get("https://stepik.org/catalog?auth=login")
time.sleep(30)
driver.quit()


