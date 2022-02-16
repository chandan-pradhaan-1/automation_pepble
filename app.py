from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import time

driver = webdriver.Chrome()
driver.get("https://www.pebblecart.com/")
account = driver.find_element_by_class_name("authorization-link")
account.click()

name = driver.find_element_by_name("login[username]")
password = driver.find_element_by_name("login[password]")
login = driver.find_element_by_name("send")

name.send_keys("chandan.pradhaan.1@gmail.com")
password.send_keys("9hKwXK6gfmu#FDH")
time.sleep(0.5)
login.click()

time.sleep(7)
driver.quit()


