import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def insta():
  
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.instagram.com")
  sleep(2)
  driver.find_element(By.XPATH ,'//input[@name="username"]').send_keys(username)
  driver.find_element(By.XPATH ,'//input[@name="password"]').send_keys(password)
  driver.find_element(By.XPATH ,'//button[@type="submit"]').click()
  sleep(5)
  driver.find_element(By.XPATH ,'//button[text()="Not Now"]').click()
  sleep(2)
  driver.find_element(By.XPATH ,'//button[text()="Not Now"]').click()
  os.system("taskkill /F /im chromedriver.exe")
 
  


insta()
