from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPageGit(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()
        
    def go_to(self):
        self.driver.get(SignInPageGit.URL)

    def try_login(self, username, password):
        # find box for input incorect username or mail
        login_elem = self.driver.find_element(By.ID, "login_field")

        #input incorect username or mail
        login_elem.send_keys(username)
        
        # find box for input incorect password 
        pass_elem = self.driver.find_element(By.ID, "password")
        
        # input incorect password
        pass_elem.send_keys(password)

        #find sing in buton 
        btn_elem = self.driver.find_element(By.NAME, "commit")

        #click sing in buton 
        btn_elem.click()
    
    def check_titel(self, exepted_title):
        return self.driver.title == exepted_title
    


