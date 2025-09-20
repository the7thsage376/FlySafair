#Day 1 notes: Code is not working as intended, but we're making some progress. 
#The aim is to enter the destination, then press enter, but that is not happening. Will troubleshoot within the coming day
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def flight_booking():l
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.flysafair.co.za/")
        
        #condition 1: clicks on round trip
        round_trip= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='searchType']")))
        round_trip.click()
        time.sleep(5)
        
        #condition 2: Departure point
        
        departure= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))  #Relative custom Xpath
        departure.send_keys("Johannesburg")
        time.sleep(5)
        
        # Destination
        destination= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='vs8__combobox']"))) #css selector
        destination.send_keys("durban")
       
        
        # Clicking departure and destination
        departure_click =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))) #Relative custom Xpath
        departure_click.click()
        time.sleep(5)
        
        destination_click= WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR,"input[aria-labelledby='vs8__combobox']")))
        destination_click.click()
        time.sleep(5)
        
     
    finally:
        driver.quit()
        
flight_booking()