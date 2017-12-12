import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

if __name__== "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com")

    #send query to search bar
    search_bar = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
    search_bar.send_keys("candy canes")

    #navigate to search
    search_button = driver.find_element_by_xpath("//div[@id='nav-search']//input[@type='submit']")
    search_button.click()

    #Wait for page to load
    time.sleep(3)

    # See if no results were found
    to_quit = False
    try:
        noresults = driver.find_element_by_xpath("//h1[@id='noResultsTitle']/span[1]")
        if noresults.text == "0":
            print("No Results found")
            to_quit = True
    except:
        pass

    if to_quit == True:
        driver.save_screenshot("failed.png")
        driver.quit()
        sys.exit()

    #Results were probably found so get the the list of results
    results_list = driver.find_elements_by_xpath("//ul[@id='s-results-list-atf']/li//div[@class='a-row']//h2")
    print("Here are the results for candy canes: ")
    print("")
    #Print Results for search candy canes
    for result in results_list:
        print(result.text)
    driver.save_screenshot("page.png")
    driver.quit()
