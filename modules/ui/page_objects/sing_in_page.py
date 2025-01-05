from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()
        
    def go_to(self):
        self.driver.get(SignInPage.URL)

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
    


class SinginpageAmazon(BasePage):
    URL = "https://www.amazon.pl/"

    def __init__(self):
        super().__init__()

    # Navigate to Amazon's main page
    def go_to_amazon(self):
        self.driver.get(SinginpageAmazon.URL)

    # Retry clicking on an element if it doesn't appear or is not clickable
    def retry_click(self, locator, max_retries=3):
        for attempt in range(max_retries):
            try:
                try:
                    self.accept_cookies()
                except TimeoutException:
                    print("Cookies banner not present on this retry.")
                link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                link.click()
                print(f"Element found and clicked on attempt {attempt + 1}")
                return
            except TimeoutException:
                print(f"Element not found. Refreshing the page. Attempt {attempt + 1} of {max_retries}.")
                self.driver.refresh()
        raise Exception("Element not found after multiple retries.")
    
    # Check if CAPTCHA appears and allow manual resolution
    def check_for_captcha(self):
        try:
            
            captcha = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "captchacharacters"))  
            )
            if captcha.is_displayed():
                print("CAPTCHA appeared. Resolve it manually, then press Enter in the terminal to continue.")
                
                input("Press Enter after resolving CAPTCHA manually...")
        except TimeoutException:
            
            print("No CAPTCHA detected. Proceeding with the test.") 

    # Accept cookies if the cookies banner appears
    def accept_cookies(self):
        try:
            cookies_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
            )
            cookies_button.click()
            print("Кукі прийнято.")
        except TimeoutException:
            print("Кукі-банер не зʼявився.")

    # Navigate to "Deals" page
    def go_to_okazje(self):
        self.retry_click((By.CSS_SELECTOR, "[href='/deals?ref_=nav_cs_gb']"))
        
    # Navigate to the first product from the "Deals" page
    def go_to_produkt(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='a-spacing-none ProductCard-module__title_awabIOxk6xfKvxKcdKDH']"))
        )
        link.click()
       
    # Add the current product to the shopping cart
    def add_to_shopping_cart(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )
        link.click()

    # Navigate to the shopping cart     
    def go_to_shoping_cart(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/cart?ref_=sw_gtc']"))
        )
        link.click()
    
    # Check the name of the product in the shopping cart
    def check_name_of_product(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="a-truncate-cut"]'))
        )
        return link.text
        
    # Check the name of the first product on the "Deals" page
    def check_first_name_of_product(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-truncate-full.a-offscreen"))
        )
        produkt_name = link.text
        return produkt_name
        