from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    def wait_for_captcha(self):
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
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='dui-truncate-5 Truncate-module_duiTruncate__EvR99']"))
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
    def get_name_of_product(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="a-truncate-cut"]'))
        )
        return link.text
        
    # Check the name of the first product on the "Deals" page
    def get_first_name_of_product(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class='dui-truncate-5 Truncate-module_duiTruncate__EvR99']"))
        )
        
        return link.text