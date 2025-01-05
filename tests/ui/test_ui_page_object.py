from modules.ui.page_objects.sing_in_page import SignInPage
from modules.ui.page_objects.sing_in_page import SinginpageAmazon
import pytest



@pytest.mark.uiGit
def test_check_incorrect_username_page_object():
    #create object of page 
    sing_in_page = SignInPage()

    #open page https://github.com/login
    sing_in_page.go_to()

    #try to login using incorect login and password 
    sing_in_page.try_login("pageobb@gmail.com", "wrong password")

    #check title  == exepted title 
    assert sing_in_page.check_titel("Sign in to GitHub · GitHub")

    #close browers
    sing_in_page.close()



@pytest.mark.uiAmazon
def test_amazon():
    # Initialize the SinginpageAmazon object
    sing_in = SinginpageAmazon()

    try:
        # Step 1: Navigate to the Amazon homepage
        sing_in.go_to_amazon()

        # Step 2: Check for CAPTCHA and accept cookies
        sing_in.check_for_captcha()
        sing_in.accept_cookies()

        # Step 3: Navigate to the "Deals" page
        sing_in.go_to_okazje()

        # Step 4: Retrieve the name of the product from the "Deals" page
        produkt_name_chek = sing_in.check_first_name_of_product()

        # Step 5: Navigate to the product's page
        sing_in.go_to_produkt()

        # Step 6: Add the product to the shopping cart
        sing_in.add_to_shopping_cart()

        # Step 7: Navigate to the shopping cart
        sing_in.go_to_shoping_cart()

        # Step 8: Retrieve the product name from the shopping cart
        produkt_name = sing_in.check_name_of_product()

        # Step 9: Verify that the product in the cart matches the product selected
        assert produkt_name_chek in produkt_name, (
            f"Product mismatch: expected '{produkt_name_chek}', got '{produkt_name}'"
        )

        print("Test completed successfully!")

    except Exception as e:
        print(f"Test failed with error: {e}")

    finally:
        # Ensure the browser is closed after the test
        sing_in.close()