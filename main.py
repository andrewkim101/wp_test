
#file test_1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
					 
# WebDriver driver = new RemoteWebDriver(new URL("http://192.168.11.108:4444/wd/hub"), capability)					 
driver = webdriver.Remote(
   command_executor="http://192.168.11.108:4444/wd/hub",
   desired_capabilities={
            "browserName": "firefox",
            })
#print ("Video: " + VIDEO_URL + driver.session_id)
  
try:
    driver.implicitly_wait(30)
    driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("documentation")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
finally:
    driver.quit()