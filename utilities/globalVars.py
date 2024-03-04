# pip install webdriver_manager
# pip install verbose
# pip install pytest_sugar
#
# pip install pulsar-client
# pip install behave
# pip install --upgrade pip
# pip install --upgrade setuptools
#

class globalVars:
    base_url = "https://www.saucedemo.com/"
    user = "standard_user"
    password = "secret_sauce"
    locked_out_user = "locked_out_user"
    error_login_message_wrong_login = "Epic sadface: Username and password do not match any user in this service"
    error_login_message_username_required = "Epic sadface: Username is required"
    error_login_message_password_required = "Epic sadface: Password is required"
    error_login_message_locked_user = "Epic sadface: Sorry, this user has been locked out."
    checkout_label = "Checkout: Your Information"

    first_name = "Victor"
    last_name = "Melo"
    postal_code = "4000"
    checkout_overview_title = "Checkout: Overview"
    completed_message = "Thank you for your order!"

    #products
    product_sauce_labs_backpack = "Sauce Labs Backpack"
    product_sauce_labs_bolt_tshirt = "Sauce Labs Bolt T-Shirt"
