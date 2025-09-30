#Day 4 notes: halfway there. Clicking enter functions 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def flight_booking():
    driver = webdriver.Chrome()
    driver.maximize_window() #Increases the size of the browser window.
    
    try:
        driver.get("https://www.flysafair.co.za/")
        
        #condition 1: clicks on one way
        #one_way= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id*='search-type-oneway']" )))
        #one_way.click()
        #time.sleep(5)
        
        #condition 2: Departure point
        
        departure= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))  #Relative custom Xpath
        departure.send_keys("Johannesburg")
        departure.send_keys(Keys.ENTER) #press enter after typing
        time.sleep(5)
        
        # Destination
        destination= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Please select destination']"))) #css selector
        destination.send_keys("durban")
        destination.send_keys(Keys.ENTER) #press enter after typing
        time.sleep(5)
        
    # Selecting the number of adults
        no_of_adults = driver.find_element(By.XPATH, "//button[normalize-space(text())='2']")
        no_of_adults.click()
        time.sleep(5)
        
    # Selecting the number of children
        no_of_kids = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='child']"))))
        no_of_kids.select_by_visible_text("3")
        time.sleep(5)
        
        # Click on the calender 
        # Works
        calender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='date-selector__input']")))
        calender.click()
        time.sleep(5)
        
        # Select the departure date
        #Almost works
        departure_date =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='4']")))
        departure_date.click()
        time.sleep(6)
    
        print(driver.page_source)
    finally:
        driver.quit()
        
flight_booking()
