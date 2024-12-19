import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



@pytest.mark.ui
def test_check_incorect_username():
    #creation obgect for control browser 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #opening page https://github.com/login
    driver.get("https://github.com/login")

    # Find field, for input incorect login or mail
    login_elem = driver.find_element(By.ID, "login_field")

    #input incorect username, login, or mail 
    login_elem.send_keys("vladyslav.sokolovskyi@mistakemail.com")
    
    # Find field, for input incorect password
    pass_elem = driver.find_element(By.ID, "password")

    #input incorect password
    pass_elem.send_keys("wrongpassword") 
  

    #find sing in buton
    btn_elem = driver.find_element(By.NAME, "commit")

    #add click for buton sign in
    btn_elem.click()
  

    #check expected name of titel
    assert driver.title == "Sign in to GitHub · GitHub"
    
    #close browser
    driver.close()
