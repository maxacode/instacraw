from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox(executable_path="geckodriver/geckodriver")
driver.get('https://www.instagram.com/madonna')

elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(1)
elm.send_keys(Keys.HOME)
time.sleep(1)
elm.send_keys(Keys.END)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox(executable_path="geckodriver/geckodriver")
driver.get('https://www.instagram.com/madonna')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
