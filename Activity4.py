from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# a) Launch the "PhpTravels" website
driver.get("https://phptravels.net/")

# b) Navigate to the "Hotels" section
hotels_section = driver.find_element(By.XPATH, "//a[contains(text(), 'Hotels')]")
hotels_section.click()

# c) Use the search functionality to find a hotel room
location_input = driver.find_element(By.ID, "s2id_location")
location_input.click()
location_input.send_keys("Dubai, United Arab Emirates")
location_input.send_keys(Keys.RETURN)

check_in_input = driver.find_element(By.NAME("checkin"))
check_in_input.clear()
check_in_input.send_keys("20/09/2022")

check_out_input = driver.find_element(By.NAME("checkout"))
check_out_input.clear()
check_out_input.send_keys("21/09/2023")

adults_input = driver.find_element(By.NAME("adults"))
adults_input.clear()
adults_input.send_keys("2")

search_button = driver.find_element(By.XPATH("//button[contains(text(), 'Search')]"))
search_button.click()

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "list_view")))

# d) Select “Movenpick Grand Al Bustan” hotel and select single room with free breakfast
hotel_name = "Movenpick Grand Al Bustan"
hotel_xpath = f"//h5[contains(text(), '{hotel_name}')]/ancestor::div[@class='room-item']"
room_select_button = driver.find_element(By.xpath(f"{hotel_xpath}//button[contains(text(), 'Book Now')]"))
room_select_button.click()

# e) Fill out the guest information form with random data and use PayPal as the payment method
guest_info_form = driver.find_element(By.ID, "details")
first_name = guest_info_form.find_element(By.NAME("firstname"))
last_name = guest_info_form.find_element(By.NAME("lastname"))
email = guest_info_form.find_element(By.NAME("email"))
phone = guest_info_form.find_element(By.NAME("phone"))
address = guest_info_form.find_element(By.NAME("address"))

# Fill in guest information with random data
first_name.send_keys("John")
last_name.send_keys("Doe")
email.send_keys("johndoe@example.com")
phone.send_keys("+1234567890")
address.send_keys("123 Main St, Cityville")

payment_method = driver.find_element(By.XPATH("//label[contains(text(), 'PayPal')]"))
payment_method.click()

confirm_booking_button = driver.find_element(By.XPATH("//button[contains(text(), 'CONFIRM THIS BOOKING')]"))
confirm_booking_button.click()

# f) Proceed with the payment on PayPal
# You need to provide the actual PayPal email and password
paypal_email = "your_paypal_email@example.com"
paypal_password = "your_paypal_password"

paypal_email_input = driver.find_element(By.ID("email"))
paypal_password_input = driver.find_element(By.ID("password"))

paypal_email_input.send_keys(paypal_email)
paypal_password_input.send_keys(paypal_password)

login_button = driver.find_element(By.ID("btnLogin"))
login_button.click()

# Wait for PayPal to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "spinner-animation")))

# Select "CREDIT UNION 1" and complete the payment
paypal_payment_method = driver.find_element(By.ID("logo"))
paypal_payment_method.click()

complete_payment_button = driver.find_element(By.ID("btnLogin"))
complete_payment_button.click()

# g) Download the receipt as a PDF
download_receipt_button = driver.find_element(By.XPATH("//button[contains(text(), 'Download Receipt')]"))
download_receipt_button.click()

# Close the web browser
driver.quit()
