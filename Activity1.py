from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Find the username and password fields, and log in
username_field = driver.find_element(By.NAME, "Username")
password_field = driver.find_element(By.NAME, "Password")

username_field.send_keys("Admin")
password_field.send_keys("admin123")

login_button = driver.find_element(By.LINK_TEXT, "Login")
login_button.click()

# Click the "Claim" section on the left side
claim_section = driver.find_element(By.NAME, "Claim")
claim_section.click()

# Click "Assign Claim"
assign_claim = driver.find_element(By.NAME, "+ Assign Claim")
assign_claim.click()

# Create a claim request for Peter Mac Anderson for travel allowance in USD
employee_field = driver.find_element(By.NAME, "Employee Name")
employee_field.send_keys("Peter Mac Anderson")
employee_field.send_keys(Keys.ENTER)

claim_type_field = driver.find_element(By.NAME, "Event")
claim_type_field.send_keys("Travel Allowance")
claim_type_field.send_keys(Keys.ENTER)

currency_field = driver.find_element(By.NAME, "Currency")
currency_field.send_keys("United States Dollars")
currency_field.send_keys(Keys.ENTER)

remarks_field = driver.find_element(By.NAME, "Remarks")
remarks_field.send_keys("Pay $100 as travel allowance")

# Add expenses for the day 2023-09-08
date_field = driver.find_element_by_id("expense_date")
date_field.send_keys("2023-09-08")

accommodation_field = driver.find_element_by_id("expense_1_amount")
accommodation_field.send_keys("$30")

fuel_allowance_field = driver.find_element_by_id("expense_2_amount")
fuel_allowance_field.send_keys("$30")

transport_field = driver.find_element_by_id("expense_3_amount")
transport_field.send_keys("$40")

# Submit
submit_button = driver.find_element_by_id("btnSave")
submit_button.click()

# Click the back button
back_button = driver.find_element_by_id("btnBack")
back_button.click()

# Close the browser
driver.quit()