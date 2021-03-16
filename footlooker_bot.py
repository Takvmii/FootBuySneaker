from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email = input('Type in your E-Mail: ')
password = input('Type in your password: ')
link = input('Type in the link of the sneaker: ')
sizeType = input('Type in your size type (EU, US, UK): ')
size = input('Type in desired size (40-43): ')

driver = webdriver.Firefox()
driver.get('https://www.footlocker.de/')
login = driver.find_element_by_xpath('//*[@id="app"]/div/header/nav[1]/div[2]/div/button')
login.click()
emailBox = driver.find_element_by_xpath('//*[@id="SignIn_email_uid"]')
passwordBox = driver.find_element_by_xpath('//*[@id="SignIn_password_password"]')
loginButton = driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/form/ul/li[3]/button')

emailBox.clear()
emailBox.send_keys(email)
passwordBox.clear()
passwordBox.send_keys(password)
loginButton.click()
time.sleep(5)
driver.get(link)

#EU UK US
sizeTypeElement = driver.find_element_by_css_selector('#ProductDetails_select_sizeChart')
driver.find_element_by_xpath('//*[@id="ProductDetails_select_sizeChart"]')
selectSizeType = Select(sizeTypeElement)
selectSizeType.select_by_value(sizeType)

#Groessenfinder
size1 = driver.find_element_by_xpath('/html/body/div[3]/div/main/div/div[2]/div/div/form/div[5]/div[3]/fieldset/div/div[1]/label')
size2 = driver.find_element_by_xpath('/html/body/div[3]/div/main/div/div[2]/div/div/form/div[5]/div[3]/fieldset/div/div[3]/label')
size3 = driver.find_element_by_xpath('/html/body/div[3]/div/main/div/div[2]/div/div/form/div[5]/div[3]/fieldset/div/div[4]/label')
size4 = driver.find_element_by_xpath('/html/body/div[3]/div/main/div/div[2]/div/div/form/div[5]/div[3]/fieldset/div/div[6]/label')

sizeLabel1 = size1.text
sizeLabel2 = size2.text
sizeLabel3 = size3.text
sizeLabel4 = size4.text

if size == sizeLabel1:
    size1.click()
if size == sizeLabel2:
    size2.click()
if size == sizeLabel3:
    size3.click()
if size == sizeLabel4:
    size4.click()
else:
    print('No size found. Please check your size!')
    driver.close()
    exit()


checkoutButton = driver.find_element_by_xpath('/html/body/div[3]/div/main/div/div[2]/div/div/form/ul/li[3]/button')
checkoutButton.click()
checkoutGet = driver.find_element_by_xpath('/html/body/div[3]/div/header/nav[2]/div[3]/a[2]')
checkoutGet.click()
payPalButton = driver.find_element_by_xpath('//*[@id="paypal-animation-content"]/div[1]/div/div/span')
payPalButton.click()
