from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Remote(
    command_executor="http://localhost:4444",
    options=webdriver.FirefoxOptions(),
)
breakpoint()

try:
    # Open the URL
    driver.get("http://www.pypi.org")

    # Wait for the search bar to be clickable
    search_bar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "search"))
    )

    # Print "pytest" in the search bar
    search_bar.send_keys("pytest")

    # Click on the search button
    search_button = driver.find_element(By.CLASS_NAME, "search-form__button")
    search_button.click()

    # Wait for the search results to appear
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "package-snippet"))
    )

    # Find 'pytest' in the list of search results and go to its page
    for package in driver.find_elements(By.CLASS_NAME, "package-snippet"):
        if "pytest" in package.text:
            package.click()
            break

    # Check that the page with the pytest library has opened
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "package-header__name"))
    )
    assert "pytest" in driver.find_element(By.CLASS_NAME, "package-header__name").text
    print("Pytest page has opened successfully.")

finally:
    # Close the browser
    driver.quit()
 

driver.close()