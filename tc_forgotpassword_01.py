from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
driver.implicitly_wait(time_to_wait=10)

#Forgotpassword

forgot_password_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
forgot_password_element.click()

#username

username_element = driver.find_element(By.NAME,value="username")
username_element.send_keys("Admin")

#Resetpassword

reset_password_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
reset_password_element.click()