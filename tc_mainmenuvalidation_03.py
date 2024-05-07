from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
driver.implicitly_wait(time_to_wait=10)


username = 'Admin'
password = 'admin123'
# Locators for Login
username_locator = 'username'
password_locator = 'password'

submitButton_locator = '//button[@type="submit"]'

webelemnt_of_username = driver.find_element(By.NAME,username_locator)
webelemnt_of_password = driver.find_element(By.NAME,password_locator)
webelemnt_of_submitButton= driver.find_element(By.XPATH,submitButton_locator)


webelemnt_of_username.send_keys(username)
webelemnt_of_password.send_keys(password)
webelemnt_of_submitButton.click()

#Click the admin_option

admin_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
assert admin_element.is_displayed() == True

#Click the pim option

pim_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
assert pim_element.is_displayed() == True

#Click the leave option

leave_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
assert leave_element.is_displayed() == True

#Click the time option

time_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
assert  time_element.is_displayed() == True

#Click the recruitment option

recruitment_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
assert recruitment_option.is_displayed() == True

#Click the myinfo option

myinfo_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
assert myinfo_option.is_displayed() == True

#Click the performance option

performance_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a')
assert performance_option.is_displayed() == True

#Click the dashboard option

dashboard_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a')
assert dashboard_option.is_displayed() == True

#Click the directory option

directory_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
assert directory_option.is_displayed() == True

#Click the maintenance option

maintenance_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
assert maintenance_option.is_displayed() == True

#Click the claim option

claim_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a')
assert claim_option.is_displayed() == True

#Click the buzz option

buzz_option = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
assert buzz_option.is_displayed() == True

print("All the Main Menu Options has been Tested Successfully!")




