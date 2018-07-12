from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

FIREFOX_PATH = '/usr/bin/firefox'
FIREFOXDRIVER_PATH = '/usr/bin/geckodriver'
WINDOW_SIZE = "1920,1080"

firefox_options = Options()  
firefox_options.add_argument("--headless")  
firefox_options.add_argument("--window-size=%s" % WINDOW_SIZE)
firefox_options.binary_location = FIREFOX_PATH

driver = webdriver.Firefox(executable_path=FIREFOXDRIVER_PATH,
                          firefox_options=firefox_options
                         ) 
driver.get("http://www.python.org")
driver.get_screenshot_as_file("title.png")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("results.png")
assert "No results found." not in driver.page_source
driver.close()