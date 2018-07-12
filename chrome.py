from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
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