from random import randint

from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class PlaceAnOrder(BASEPAGE):
    locator_dictionary = {
        "men_nav_option": (By.XPATH, './/span[text() = "Men"]'),
        "men_clothing_option": (By.XPATH, './/a[text() = " Clothing"]'),
        "records_per_page": (By.XPATH, '(.//select[@id="limiter"]/option[4])[1]'),
        "amount_max": (By.XPATH, './/input[@class = "am-filter-price -to input-text"]'),
        "go_btn": (By.CLASS_NAME, 'am-filter-go'),
        "item_name": (By.XPATH, './/h6/a'),
        "item_name_on_pdp": (By.CLASS_NAME, 'base'),
        "payment_info": (By.XPATH, './/div[@class = "payment_info"]/span'),
        "add_to_cart_btn": (By.ID, 'product-addtocart-button'),
        "error_msg": (By.XPATH, './/div[@data-ui-id = "message-error"]/div[text() = "This product is out of stock."]'),
        "error_msg_2": (By.XPATH, './/div[@data-ui-id = "message-error"]/div[text() = "The requested qty is not '
                                  'available here"]'),
        "proceed_to_checkout_btn": (By.XPATH, './/button[text() = "Proceed to Checkout"]'),

        "address_email": (By.ID, 'customer-email'),
        "first_name": (By.XPATH, './/input[@name = "firstname"]'),
        "last_name": (By.XPATH, './/input[@name = "lastname"]'),
        "phone": (By.XPATH, '(.//input[@name = "telephone"])[2]'),
        "address": (By.XPATH, './/input[@name = "street[0]"]'),
        "city": (By.XPATH, './/input[@name = "city"]'),
        "company": (By.XPATH, './/input[@name = "company"]'),
        "additional_register": (By.XPATH, './/div[@class = "admin__field admin__field-option"][2]'),

        "cod_radio_btn": (By.XPATH, './/label[@for= "cashondelivery"]'),
        "place_order_btn": (By.XPATH, '//*[@id="checkout"]/div[5]/div[3]/div/div[5]/div/div/button'),
        "order_number": (By.XPATH, './/p[1]/span'),
        "order_number_after_login": (By.XPATH, './/a[@class = "order-number"]/strong'),
        "print_invoice_btn": (By.XPATH, './/*[@class = "nav item"]/a[text() = "Print"]')
    }

    constants = {
        "order_no_title": "Order # 234",
        "men_page_title": "Men's Fashion",
        "men_clothing_title": "Clothing for Men | A form of Self Expression | Brandrange",
        "per_page_filter_url": "product_list_limit=54",
        "filtered_url": "price=0-1000&product_list_limit=54",
        "checkout_page_title": "Checkout"
    }
    urls = {
        "Home": '/'
    }

    def go_to(self, link):
        base_url = get_setting("URL", "url")
        self.browser.get(base_url + self.urls[link])
        if self.browser.title == self.constants["home_page_title"]:
            return True
        else:
            return False

    def navigate_to_plp(self):
        time.sleep(3)
        self.hover_over_element(self.find_element(self.locator_dictionary["men_nav_option"]))
        time.sleep(1)
        self.click_element(self.find_element(self.locator_dictionary["men_clothing_option"]))
        assert self.browser.title == self.constants[
            "men_clothing_title"], "The user is not navigated to the men clothing plp "

    def filter_records_per_page(self, records_per_page):
        self.click_element(self.find_element(self.locator_dictionary["records_per_page"]))
        assert self.constants["per_page_filter_url"] in self.browser.current_url, "Issue: Total number of records: " + records_per_page + " did not appear."

    def apply_filter(self, amount_max, payment_info):
        self.find_element(self.locator_dictionary["amount_max"]).clear()
        self.send_text_to_element(self.find_element(self.locator_dictionary["amount_max"]), amount_max)
        # self.click_element(self.find_element(self.locator_dictionary["records_per_page"]))
        time.sleep(2)
        self.click_element(self.find_element(self.locator_dictionary["go_btn"]))
        assert self.constants["filtered_url"] in self.browser.current_url, "Issue: The filter was not applied."

    def select_an_item(self, random_item):
        # random_number = 2
        random_number = randint(1, 54)
        element_xpath = "(.//h6/a)[" + str(random_number) + "]"
        the_element = self.find_element((By.XPATH, element_xpath))
        element_name = self.get_element_text(the_element)
        self.click_element(the_element)
        assert element_name == self.get_element_text(self.find_element(self.locator_dictionary[
                                                                           "item_name_on_pdp"])), "Issue: The user is not navigated to selected products screen "
    # def select_an_item2(self, random_item):
    #     random_number = 5
    #     # random_number = randint(1, 24)
    #     element_xpath = "(.//h6/a)[" + str(random_number) + "]"
    #     the_element = self.find_element((By.XPATH, element_xpath))
    #     element_name = self.get_element_text(the_element)
    #     self.click_element(the_element)
    #     assert element_name == self.get_element_text(self.find_element(self.locator_dictionary[
    #                                                                        "item_name_on_pdp"])), "Issue: The user is not navigated to selected products screen "

    def verify_payment_method(self):
        time.sleep(2)
        is_available = 0
        while is_available != 1:
            if self.get_element_text(self.find_element(self.locator_dictionary["payment_info"])) == "COD Available":
                is_available = 1
                pass
            else:
                print("Issue: The selected PDP is not COD product ")
                self.browser.back()
                self.select_an_item("")
                self.verify_payment_method()

    def add_item_to_cart(self, add_to_cart_btn):
        time.sleep(2)
        is_available = 0
        while is_available != 1:
            # self.click_element(self.find_element(self.locator_dictionary["add_to_cart_btn"]))
            # WebDriverWait(self.browser, 5).until(
            #     EC.invisibility_of_element((By.CLASS_NAME, 'mfp-container mfp-s-ready mfp-inline-holder')))
            self.browser.execute_script("arguments[0].click();", self.find_element(self.locator_dictionary["add_to_cart_btn"]))
            if self.is_element_displayed(self.locator_dictionary["proceed_to_checkout_btn"]):
                is_available = 1
            else:
                self.browser.back()
                self.select_an_item("")
                self.verify_payment_method()
                self.add_item_to_cart(add_to_cart_btn)

    def proceed_to_checkout(self, proceed_to_checkout_btn, checkout_screen):
        time.sleep(2)

        # WebDriverWait(self.browser, self.WAIT).until(EC.invisibility_of_element((By.CLASS_NAME, 'mfp-container
        # mfp-s-ready mfp-inline-holder'))) self.browser.execute_script("arguments[0].click();", WebDriverWait(
        # self.browser, self.WAIT).until( EC.element_to_be_clickable(self.locator_dictionary[]))) WebDriverWait(
        # self.browser, self.WAIT).until(EC.element_to_be_clickable(self.locator_dictionary[
        # "proceed_to_checkout_btn"])).click()
        self.browser.execute_script("arguments[0].click();",
                                    self.find_element(self.locator_dictionary["proceed_to_checkout_btn"]))
        # self.click_element(self.find_element(self.locator_dictionary["proceed_to_checkout_btn"]))
        assert self.browser.title == self.constants[
            "checkout_page_title"], "The user is not navigated to Checkout screen."

    def checkout(self, place_order_btn, is_login, success_screen):
        if is_login == 0:
            self.fill_address("tester@testing.com", "QA", "team", "501234567", "123 test road", "test city",
                              "BR - QA team")
        time.sleep(2)
        self.click_element(self.find_element(self.locator_dictionary["cod_radio_btn"]))
        time.sleep(2)
        self.click_element(self.find_element(self.locator_dictionary["place_order_btn"]))
        time.sleep(10)
        if is_login == 0:
            order_number = self.get_element_text(self.find_element(self.locator_dictionary["order_number"]))
        else:
            order_number = self.get_element_text(self.find_element(self.locator_dictionary["order_number_after_login"]))
        order_number = "Order # " + order_number
        print(order_number)
        assert self.browser.title == order_number, "Issue: The order was not placed."

    def fill_address(self, email, f_name, l_name, phone, address, city, company):
        self.send_text_to_element(self.find_element(self.locator_dictionary["address_email"]), email)
        self.send_text_to_element(self.find_element(self.locator_dictionary["first_name"]), f_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["last_name"]), l_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["phone"]), phone)
        self.send_text_to_element(self.find_element(self.locator_dictionary["address"]), address)
        self.send_text_to_element(self.find_element(self.locator_dictionary["city"]), city)
        self.send_text_to_element(self.find_element(self.locator_dictionary["company"]), company)
        self.click_element(self.find_element(self.locator_dictionary["additional_register"]))

