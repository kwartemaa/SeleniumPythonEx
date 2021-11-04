from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path="C:\Program Files\Drivers\geckodriver\geckodriver.exe")
# driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Ie(executable_path="C:\Program Files\Drivers\iedriver\IEDriverServer.exe")
driver.get("https://www.facebook.com/")
print(driver.title)
driver.close()
