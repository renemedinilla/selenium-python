from selenium import webdriver
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
driver.get("https://www.google.com")
driver.get_screenshot_as_file("capture.png")
driver.close()