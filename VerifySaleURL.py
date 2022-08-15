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
driver.find_element(By.LINK_TEXT,"Remind Me Later").click()
driver.find_element(By.CLASS_NAME,'switch-to-lightning').click()
driver.get('https://360degreecloudtechnologie36-dev-ed.lightning.force.com/lightning/page/home?0.source=alohaHeader')
l= driver.current_url
print("Current url is: " + l)
driver.close()


