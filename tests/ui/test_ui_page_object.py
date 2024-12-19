from modules.ui.page_objects.sing_in_page import SignInPage
import pytest



@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #create object of page 
    sing_in_page = SignInPage()

    #open page https://github.com/login
    sing_in_page.go_to()

    #try to login using incorect login and password 
    sing_in_page.try_login("pageobb.gmail.com", "wrong password")

    #check title  == exepted title 
    assert sing_in_page.check_titel("Sign in to GitHub · GitHub")

    #close browers
    sing_in_page.close()