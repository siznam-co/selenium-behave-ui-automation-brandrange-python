import time

from behave import *
from pageobjects.BrandRange import BrandRange
from pageobjects.PlaceAnOrder import PlaceAnOrder


@given('User is on "{home}" Page.')
def step_impl(context, home):
    var = BrandRange(context).go_to(home)
    assert var, "The user is not navigated to " + home + " screen."


@when('the user clicks profile icon and selects "{sign_in_option}" option, he will be moved to "{sign_in_page}" Page')
def step_impl(context, sign_in_option, sign_in_page):
    var = BrandRange(context).go_to_login_page(sign_in_option, sign_in_page)
    assert var, "The user is not navigated to " + sign_in_page + " screen."


@when(
    'the user provide valid credentials: UN: "{username}", PW: "{password}" and click "{sign_in_btn}" button, '
    'he/she will be moved to "{home_screen}" screen.')
def step_impl(context, username, password, sign_in_btn, home_screen):
    var = BrandRange(context).sign_in(username, password, sign_in_btn)
    assert var, "The user is not logged in and navigated to " + home_screen + " screen."


@when('the user clicks profile icon and selects "{sign_up_option}" option, he will be moved to "{sign_up_page}" Page.')
def step_impl(context, sign_up_option, sign_up_page):
    var = BrandRange(context).go_to_signup_page(sign_up_option, sign_up_page)
    assert var, "The user is not navigated to " + sign_up_page + " screen."


@when(
    'the user enters sign up detail, and click "{register_btn}" button, he/she will be moved to his "{'
    'account_screen}" screen after login.')
def step_impl(context, register_btn, account_screen):
    var = BrandRange(context).sign_up("john4", "qwerty", "test4@testing.com", "501234567", "Qwertyuiop123",
                                      register_btn)
    assert var, "The user is not navigated to " + account_screen + " screen."


@step('the user navigates to "{clothing_section}" section of Men.')
def step_impl(context, clothing_section):
    PlaceAnOrder(context).navigate_to_plp()


@step('the user filters "{records_per_page}" records per page.')
def step_impl(context, records_per_page):
    PlaceAnOrder(context).filter_records_per_page(records_per_page)

@when('the user sets the max amount filter to "{amount_max}", all the "{payment_info}" items should appear.')
def step_impl(context, amount_max, payment_info):
    PlaceAnOrder(context).apply_filter(amount_max, payment_info)


@when('the user clicks any "{random_item}" item\'s name, he navigates to the selected item pdp.')
def step_impl(context, random_item):
    PlaceAnOrder(context).select_an_item(random_item)


@step("the user verifies the payment method.")
def step_impl(context):
    PlaceAnOrder(context).verify_payment_method()


@when('the user clicks on "{add_to_cart_btn}" button, a popup overley appears. But if item is out of stock the user '
      'will go back and repeat above steps.')
def step_impl(context, add_to_cart_btn):
    PlaceAnOrder(context).add_item_to_cart(add_to_cart_btn)


@when('the user clicks "{proceed_to_checkout_btn}" button, the user will be navigated to the "{checkout_screen}" '
      'screen.')
def step_impl(context, proceed_to_checkout_btn, checkout_screen):
    PlaceAnOrder(context).proceed_to_checkout(proceed_to_checkout_btn, checkout_screen)


@when(
    'the user selects payment method and clicks the "{place_order_btn}" button, the order will be placed and the user '
    'will '
    'be navigated to the "{success_screen}" screen.')
def step_impl(context, place_order_btn, success_screen):
    PlaceAnOrder(context).checkout(place_order_btn, 1, success_screen)


@when(
    'the user adds address, selects payment method and clicks the "{place_order_btn}" button, the order will be placed and '
    'the user will be navigated to the "{success_screen}" screen.')
def step_impl(context, place_order_btn, success_screen):
    PlaceAnOrder(context).checkout(place_order_btn, 0, success_screen)
