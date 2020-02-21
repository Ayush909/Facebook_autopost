from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#disables the popups in chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
#opens facebook
driver.get("https://www.facebook.com")
#types your email
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('Your email address')
#types your password
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('Your password')
#clicks login button
button =driver.find_element_by_xpath('//*[@id="loginbutton"]')
button.click()
#reads content of file 'quotes_file.txt'

with open('quotes_file.txt') as myfile:
    data = myfile.read()
#types content of file into post box of facebook
post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys(data)

time.sleep(5)
#clicks the post button
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()


