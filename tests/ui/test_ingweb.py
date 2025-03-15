import pytest
from playwright.sync_api import Page, expect
from modules.ui.page_objects.ing_playwright import Ing
from login_generator import random_login


@pytest.mark.Ingsearch
def test_search(page: Page):
    search_page = Ing(page)
    search_page.navigate()
    search_page.search("kredyt")
    search_page.akcept_cooki()

    try:
        search_page.check_title()
        print("Test complite")
    except AssertionError as e:
        print ("Test failed with error: {e}")


@pytest.mark.Ingtrylogin
def test_login(page: Page):
    login_page = Ing(page)
    login_page.navigate()
    login_page.try_login(login = random_login(6,4))
    
    try:
        login_page.chek_title_login()
    except AssertionError as e:
        print ("Test failed with error: {e}")

    


