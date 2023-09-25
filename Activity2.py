from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# a) Navigate to the provided URL
driver.get("https://demo.opencart.com/")

# b) Use the search bar to search for a product
search_input = driver.find_element(By.CSS_SELECTOR, "input[name='search']")
search_input.send_keys("iPhone")
search_input.send_keys(Keys.RETURN)

# Wait for the search results page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-layout")))

# c) Click on one of the product links to view product details
product_link = driver.find_element(By.CSS_SELECTOR, ".product-layout .product-thumb")
product_link.click()

# d) Add the product to the shopping cart
add_to_cart_button = driver.find_element(By.ID, "button-cart")
add_to_cart_button.click()

# Wait for the product to be added to the cart
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cart-total")))

# e) Navigate to the shopping cart and verify the product
shopping_cart_link = driver.find_element(By.ID, "cart-total")
shopping_cart_link.click()

# f) Proceed to the checkout process
checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary[href*='checkout']")
checkout_button.click()

# Wait for the checkout page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "collapse-checkout-option")))

# g) Fill in the billing details with fictitious information
billing_firstname = driver.find_element(By.ID, "input-payment-firstname")
billing_firstname.send_keys("John")

billing_lastname = driver.find_element(By.ID, "input-payment-lastname")
billing_lastname.send_keys("Doe")

billing_address = driver.find_element(By.ID, "input-payment-address-1")
billing_address.send_keys("123 Main St")

billing_city = driver.find_element(By.ID, "input-payment-city")
billing_city.send_keys("Cityville")

billing_postcode = driver.find_element(By.ID, "input-payment-postcode")
billing_postcode.send_keys("12345")

billing_country = driver.find_element(By.ID, "input-payment-country")
billing_country.send_keys("United States")

billing_region = driver.find_element(By.ID, "input-payment-zone")
billing_region.send_keys("New York")
billing_region.send_keys(Keys.ENTER)

# h) Choose a shipping method
shipping_method = driver.find_element(By.NAME, "shipping_method")
shipping_method.click()

# i) Select a payment method (e.g., Cash On Delivery)
payment_method = driver.find_element(By.NAME, "payment_method")
payment_method.click()

# j) Place the order
order_button = driver.find_element(By.ID, "button-payment-method")
order_button.click()

# k) Verify the order confirmation
confirmation_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
)

print("Order Confirmation Message:", confirmation_message.text)

# Close the browser
driver.quit()
