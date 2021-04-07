Feature: BrandRange

  @smoke_test
  Scenario: Register as a new user
    Given User is on "Home" page.
    When the user clicks profile icon and selects "Register" option, he will be moved to "Sign Up" Page.
    When the user enters sign up detail, and click "REGISTER" button, he/she will be moved to his "Account" screen after login.

  @smoke_test
  Scenario: The user sign in and place an order for COD product and checkout
    Given User is on "Home" page.
    When the user clicks profile icon and selects "Sign In" option, he will be moved to "Sign In" Page
    When the user provide valid credentials: UN: "john@123.com", PW: "Qwertyuiop123" and click "SIGN IN" button, he/she will be moved to "Home" screen.
    And the user navigates to "Clothing" section of Men.
    And the user filters "54" records per page.
    When the user sets the max amount filter to "1000", all the "COD Available" items should appear.
    When the user clicks any "random" item's name, he navigates to the selected item pdp.
    And the user verifies the payment method.
    When the user clicks on "ADD TO CART" button, a popup overley appears. But if item is out of stock the user will go back and repeat above steps.
    When the user clicks "PROCEED TO CHECKOUT" button, the user will be navigated to the "Checkout" screen.
    When the user selects payment method and clicks the "PLACE ORDER" button, the order will be placed and the user will be navigated to the "Success" screen.

  @smoke_test
  Scenario: User place an order for COD product and checkout
    Given User is on "Home" page.
    And the user navigates to "Clothing" section of Men.
    And the user filters "54" records per page.
    When the user sets the max amount filter to "1000", all the "COD Available" items should appear.
    When the user clicks any "random" item's name, he navigates to the selected item pdp.
    And the user verifies the payment method.
    When the user clicks on "ADD TO CART" button, a popup overley appears. But if item is out of stock the user will go back and repeat above steps.
    When the user clicks "PROCEED TO CHECKOUT" button, the user will be navigated to the "Checkout" screen.
    When the user adds address, selects payment method and clicks the "PLACE ORDER" button, the order will be placed and the user will be navigated to the "Success" screen.

