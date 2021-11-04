
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
print(driver.title)


 # CSS selector tutorial
