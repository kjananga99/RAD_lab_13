from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# URLs for the two movies or TV shows you want to search for
urls_to_search = [
    "https://www.imdb.com/",
    "https://www.imdb.com/"
]

# Movie or TV show names you want to search for
search_queries = [
    "The Matrix",
    "Inception"  # Replace with the title of the second movie/TV show
]

# Loop through the URLs and search queries
for i in range(len(urls_to_search)):
    # a) Navigate to the IMDb website
    driver.get(urls_to_search[i])

    # b) Use the search bar to search for a movie or TV show
    search_bar = driver.find_element(By.ID, "suggestion-search")
    search_bar.clear()
    search_bar.send_keys(search_queries[i])
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "findResult")))

    # c) Click on the search result corresponding to the movie or TV show
    search_results = driver.find_elements(By.CLASS_NAME, "findResult")
    search_results[0].click()

    # d) Retrieve movie/TV show information
    title = driver.find_element(By.XPATH, "//h1")
    release_year = driver.find_element(By.CSS_SELECTOR, "a[href*='/year/']")
    imdb_rating = driver.find_element(By.CLASS_NAME, "ratingValue")
    description = driver.find_element(By.CSS_SELECTOR, ".summary_text")
    cast_list = driver.find_elements(By.XPATH, "//table[@class='cast_list']//tr/td[2]")

    # Extract and print the information
    print("Title:", title.text.strip())
    print("Release Year:", release_year.text.strip())
    print("IMDb Rating:", imdb_rating.text.strip())
    print("Description/Plot:", description.text.strip())
    print("Cast:")
    for actor in cast_list[:10]:
        print(actor.text.strip())

    # f) Click on the "See full cast" button to view the complete cast list
    full_cast_button = driver.find_element(By.CLASS_NAME, "see-more")
    full_cast_button.click()

    # Wait for the full cast page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cast_list")))

    # g) Retrieve and print the names of the first 10 cast members
    full_cast_list = driver.find_elements(By.XPATH, "//table[@class='cast_list']//tr/td[2]")
    print("Full Cast (First 10):")
    for actor in full_cast_list[:10]:
        print(actor.text.strip())

    # h) Navigate back to the search results page
    driver.back()

# j) After completing both searches, close the browser
driver.quit()
