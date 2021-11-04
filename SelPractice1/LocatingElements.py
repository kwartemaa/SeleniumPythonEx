import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class FindingElementByIDOrXpath:
    def look_for_id(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('test@test.com')
        time.sleep(5)

    def look_for_xpath(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_xpath("//input[@id='login-input']").send_keys('test@test1.com')
        time.sleep(5)

    def look_for_link_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_link_text("Yatra for Business").click()
        time.sleep(5)


find_element = FindingElementByIDOrXpath()
# find_element.look_for_id()
# find_element.look_for_xpath()
find_element.look_for_link_text()
