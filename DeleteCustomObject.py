from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option1 =Options()
option1.add_argument("--disable-notificatios")


driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe",chrome_options=option1);
driver.maximize_window()
driver.get("https://login.salesforce.com/");
driver.find_element(By.ID,'username').send_keys('automationvarsha12@gmail.com')
driver.find_element(By.ID,'password').send_keys('Auto@123')
driver.find_element(By.ID,"Login").click()
driver.find_element(By.LINK_TEXT,"Remind Me Later").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//ul[@class="tabBarItems slds-grid"]//a[@title="Object Manager"]').click()
driver.find_element(By.ID,'globalQuickfind').send_keys('custome12')
#xpath  //input[@id='globalQuickfind']
driver.find_element(By.LINK_TEXT,"Custome12").click() # //a[normalize-space()="Custome12"][1]
driver.find_element(By.XPATH,'//span[contains(text(),"Delete")]').click()
driver.find_element(By.XPATH,'(//span[contains(@class,"label bBody")][normalize-space()="Delete"])[2]').click()

