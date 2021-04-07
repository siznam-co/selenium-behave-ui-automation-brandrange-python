from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class BrandRange(BASEPAGE):
    locator_dictionary = {
        "profile_icon_locator": (By.ID, 'switcher-myaccount-trigger'),
        "sign_in_option": (By.CLASS_NAME, 'authorization-link'),
        "sign_up_option": (By.XPATH, './/a[text() = "Register"]'),
        "title_of_login_page": (By.XPATH, './/h1/span[text()= "Customer Login"]'),
        "email": (By.NAME, 'login[username]'),
        "password": (By.NAME, 'login[password]'),
        "sign_in_btn": (By.NAME, 'send'),
        "title_of_signup_page": (By.XPATH, './/h1/span[text()= "Create New Customer Account"]'),
        "first_name": (By.ID, 'firstname'),
        "last_name": (By.ID, 'lastname'),
        "signup_email": (By.ID, 'email_address'),
        "phone": (By.ID, 'phone_number'),
        "signup_password": (By.ID, 'password'),
        "confirm_password": (By.ID, 'password-confirmation'),
        "register_btn": (By.XPATH, './/button[@type = "submit"]'),
        "add_to_cart_btn": (By.ID, 'product-addtocart-button')
    }

    constants = {
        "Sign In": "title_of_login_page",
        "SIGN IN": "sign_in_btn",
        "REGISTER": "register_btn",
        "Home": "home_page_title",
        "profile_icon": "profile_icon_locator",
        "home_page_title": "Brandrange: Shop Branded Dresses, Bags, Toys, Shoes",
        "sign_in_page_title": "Customer Login",
        "sign_up_page_title": "Create New Customer Account",
        "account_page_title": "My Account"
    }
    urls = {
        "Sign In": '/customer/account/login/',
        "Home": '/',
        "Gucci": '/gucci-accessories-belts---blue-27504.html'
    }

    def go_to(self, link):
        base_url = get_setting("URL", "url")
        self.browser.get(base_url + self.urls[link])
        if self.browser.title == self.constants["home_page_title"]:
            return True
        else:
            return False

    def go_to_login_page(self, sign_in_option, sign_in_page):
        self.click_element(self.find_element(self.locator_dictionary["profile_icon_locator"]))
        self.click_element(self.find_element(self.locator_dictionary["sign_in_option"]))
        if self.browser.title == self.constants["sign_in_page_title"]:
            return True
        else:
            return False

    def click_on(self, element):
        self.click_element(
            self.find_element(self.locator_dictionary[self.constants[element]])
        )

    def sign_in(self, username, password, sign_in_btn):
        self.send_text_to_element(self.find_element(self.locator_dictionary["email"]), username)
        self.send_text_to_element(self.find_element(self.locator_dictionary["password"]), password)
        self.click_on(sign_in_btn)
        if self.browser.title == self.constants["home_page_title"]:
            return True
        else:
            return False

    def go_to_signup_page(self, sign_up_option, sign_up_page):
        self.click_element(self.find_element(self.locator_dictionary["profile_icon_locator"]))
        self.click_element(self.find_element(self.locator_dictionary["sign_up_option"]))
        if self.browser.title == self.constants["sign_up_page_title"]:
            return True
        else:
            return False

    def sign_up(self, first_name, last_name, email, phone, password, register_btn):
        self.send_text_to_element(self.find_element(self.locator_dictionary["first_name"]), first_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["last_name"]), last_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["signup_email"]), email)
        self.send_text_to_element(self.find_element(self.locator_dictionary["phone"]), phone)
        self.send_text_to_element(self.find_element(self.locator_dictionary["signup_password"]), password)
        self.send_text_to_element(self.find_element(self.locator_dictionary["confirm_password"]), password)
        self.click_on(register_btn)
        if self.browser.title == self.constants["account_page_title"]:
            return True
        else:
            return False
