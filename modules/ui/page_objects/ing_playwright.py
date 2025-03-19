from playwright.sync_api import Page, expect
from data_for_test import Buton_selectors, name_title_new_page,Buton_selectors_premium,name_title_new_page_premium
import time



class Ing:
    def __init__(self, page: Page):
        self.page = page
        self.search_term_input = self.page.locator('#headerSearchControl')
        self.search_cookie = self.page.locator(".js-cookie-policy-main-decline-button")

    def navigate(self):
        url = "https://www.ing.pl/"
        self.page.goto(url)

    def search(self, text): 
        
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")
    
    def check_title(self):
        expect(self.page.get_by_role("heading", name="Wyniki wyszukiwania")).to_contain_text("Wyniki")

    def akcept_cooki(self):
        if self.search_cookie.is_visible():
            self.search_cookie.click()
    
    def try_login(self, login):
        self.page.get_by_role("button", name="Zaloguj").click()
        self.page.get_by_role("link", name="Moje ING Zaloguj do aplikacji").click()
        self.page.get_by_role("button", name="Odrzuć").click()
        self.page.get_by_role("textbox", name="Login do bankowości Moje ING").fill(login)
        self.page.get_by_role("button", name="Dalej").click()

    def chek_title_login(self):
        expect(self.page.get_by_text("Logujesz się do bankowości")).to_contain_text("Logujesz")

    def click_butons(self):
        for index, buton_selector in enumerate(Buton_selectors):
            self.akcept_cooki()
            self.page.get_by_role("link", name= buton_selector, exact=True).nth(0).click()
            title_name = name_title_new_page[index]
            expect(self.page.locator("h1").nth(0)).to_contain_text(title_name)
            time.sleep(0.5)
       
    def click_butons_premium(self):
        self.page.get_by_role("link", name="Premium").click()
        for index, buton_selector in enumerate(Buton_selectors_premium):
            self.akcept_cooki()
            self.page.get_by_role("link", name= buton_selector, exact=True).nth(0).click()
            title_name = name_title_new_page_premium[index]
            expect(self.page.locator("h1").nth(0)).to_contain_text(title_name)
            time.sleep(0.5)
    