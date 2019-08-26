
#file test_1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import platform
class MainTest(unittest.TestCase):

	@classmethod
	def setUp(cls):

		options = Options()
		options.headless = True
		if platform.system() == 'Windows':
			cls.driver = webdriver.Chrome('./win/chromedriver.exe',options=options)
		else:
			cls.driver = webdriver.Chrome('./linux/chromedriver',options=options)

	# WebDriver driver = new RemoteWebDriver(new URL("http://192.168.11.108:4444/wd/hub"), capability)					 
	# driver = webdriver.Remote(
	#    command_executor="http://192.168.11.108:4444/wd/hub",
	#    desired_capabilities={
	#             "browserName": "firefox",
	#             })
	# #print ("Video: " + VIDEO_URL + driver.session_id)

	def test_python(self):
		self.driver.implicitly_wait(30)
		self.driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
		self.driver.get("http://wp.houseofkim.info")
		elem = self.driver.find_element_by_xpath('//*[@id="masthead"]/div[1]/div[2]/div/div/h1/a')
		self.assertTrue('WP' in elem.text)
	
	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)