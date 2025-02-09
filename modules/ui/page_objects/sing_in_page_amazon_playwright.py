
from playwright.sync_api import Page,  expect

class Amazon():
    def go_to(self, page: Page ):
        page.goto("https://www.amazon.pl/")
        page.get_by_role("button", name="Akceptuj").click()
        page.get_by_label("Główny").get_by_role("link", name="Okazje").click()
        page.get_by_test_id("B0DCBB2YTR").click()
        page.get_by_title("Dodaj do koszyka").click()
        page.locator("#sw-gtc").get_by_role("link", name="Przejdź do koszyka").click()

    def check_name(self,page:Page, name):
       
        expect(page.locator("h4")).to_contain_text(name)
        
     
    def close(self,page:Page):
        page.close()
    
       


