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

Pim_menu_option_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
Pim_menu_option_element = driver.find_element(By.XPATH, Pim_menu_option_xpath)

Pim_menu_option_element.click()

#Click the User Management Option

user_management_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
user_management_element.click()

#Click the Job Option
job_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
job_element.click()

#Click the Organization Option
organization_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
organization_element.click()

#Click the Qualification Option
qualifications_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
qualifications_element.click()

#Click the Nationalities Option
nationalities_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')
nationalities_element.click()

#Click the Corporate Banking Option
corporate_banking_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a')
corporate_banking_element.click()

#Click the Configuration Option
configuration_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
configuration_element.click()

print(" All the Header Options has been Tested Successfully!")

