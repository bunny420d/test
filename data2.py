from	selenium	import	*
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options


#s = Service('C:\\Program Files\\Python310\\geckodriver.exe')

options = Options()
#options.headless = True



binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#browser	=	webdriver.Firefox(options=options, service=s)
browser	=	webdriver.Firefox(options=options, firefox_binary=binary)


try:
    browser.get("https://data.simulationiq.com/app/account#/login")
    userElem	=	browser.find_element(By.ID, 'username')
    userElem.send_keys('cholleran@wustl.edu') #admn no here
    # time.sleep(5)
    passwordElem	=	browser.find_element(By.ID, 'password')
    passwordElem.send_keys('WUSTL10!') # password here
    time.sleep(0.05)
    loginElem	=	browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/form/button/span')
    loginElem.click()
    time.sleep(10)
    login = browser.current_url
    time.sleep(10)
    accountElem	=	browser.find_element(By.XPATH, '//*[@id="3"]/div/div[3]/div')
    accountElem.click()
    time.sleep(2)

    logoutElem	=	browser.find_element(By.XPATH, '/html/body/data-menu/div/div/div/div/div[4]/div/div[1]')
    logoutElem.click()

    if login == 'https://data.simulationiq.com/app/main#/home':
        print('0')
    else:
        print('1')
#	count = count+1
except NoSuchElementException:
	print('2')
except WebDriverException:
	print('3')
except NoSuchWindowException:
	print('3')

finally:
	browser.quit()