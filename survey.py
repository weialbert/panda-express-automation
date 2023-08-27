import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# define helper function to click on next button
def click_next(driver):
    driver.find_element("id", "NextButton").click()
    time.sleep(0.5)

def setup():
    # Get user input
    user_input = '4yJ9kG8E2TnS1cN0D3W5A7'
    user_email = input('Enter your email address: ')

    # Set up ChromeDriver
    service = ChromeService()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the Panda Express survey website
    driver.get('https://www.pandaexpress.com/feedback')

    # Find the survey code text box and enter user input
    code = driver.find_element("id", "CN1")
    code.click()
    code.send_keys(user_input)

    # Pressing next 3 times with any code will enter the survey
    for i in range(3):
        click_next(driver)

    return driver, user_email

def fill_survey(email_addr, driver):
    # See if there is a next button available
    nextLink = driver.find_elements(By.ID, "NextButton")

    while len(nextLink) != 0:
        # Find options
        optionButton = driver.find_elements(By.CLASS_NAME, "radioSimpleInput")

        # Find Email prompt
        email = driver.find_elements(By.NAME, "S000057")
        if len(email) != 0:
            email = email[0].send_keys(email_addr)
            email = driver.find_element(By.NAME, "S000064").send_keys(email_addr)
            nextLink = driver.find_elements(By.ID, "NextButton")[0].click()
            break

        # Click on an option
        for i in range(0, len(optionButton), 5):
            optionButton[i].click()

        # Find next button and click if applicable
        nextLink = driver.find_elements(By.ID, "NextButton")
        if len(nextLink) == 0:
            break
        nextLink[0].click()

def main():
    # setup driver and navigate to survey
    driver, email_addr = setup()

    # fill out the survey
    fill_survey(email_addr, driver)

    # Close the browser window
    driver.quit()

    # Print
    print("Done! Check your email address ({}) shortly!".format(email_addr))

if __name__ == '__main__':
    # Entry point of the script
    main()