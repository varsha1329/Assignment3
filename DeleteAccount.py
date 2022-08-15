from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option1 =Options()
option1.add_argument("--disable-notifications")


driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe",chrome_options=option1);
driver.maximize_window()
driver.get("https://login.salesforce.com/");
driver.find_element(By.ID,'username').send_keys('automationvarsha12@gmail.com')
driver.find_element(By.ID,'password').send_keys('Auto@123')
driver.find_element(By.ID,"Login").click()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Remind Me Later").click()
driver.find_element(By.XPATH,'//a[@title="Accounts Tab"]').click()
driver.find_element(By.XPATH,'//div[@class="topLeft"]//a[@title="Close"]').click()
driver.find_element(By.XPATH,'//div[@class="pbBody"]//a[contains(text(),"Varsha New Account")]').click()
driver.find_element(By.XPATH,'//td[@id="bottomButtonRow"]//input[@title="Delete"]').click()



