import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#Create phantomjs webdriver and navigate to job listing page at kent
driver = webdriver.PhantomJS('phantomjs')
driver.get("http://jobs.kent.edu/cw/en-us/listing/")
num_of_listings = 0
while True:
	#Rudimentary way to populate all results_list
	#Continues to click the More Jobs link until the number of elements on the jobs_table
	#ceases to increase or until the more jobs link is gone
	try:
		time.sleep(1)
		button = driver.find_element_by_xpath("//div[@id='recent-jobs']/p")
		click_button = ActionChains(driver)\
			.click(button)
		click_button.perform()
		time.sleep(1)
		table = driver.find_elements_by_xpath("//tbody[@id='recent-jobs-content']/tr")
		if len(table) > num_of_listings:
			num_of_listings = len(table)
		else:
			break
	except:
		break
jobs = driver.find_elements_by_xpath("//tbody[@id='recent-jobs-content']/tr")

i = 0
for job in jobs:
	#Attempts to locate the table data containing the department
	dept = None
	try:
		dept = job.find_element(By.XPATH, "./td[3]")
	except:
		continue #this row does not contain a job listing

	#If that table data contains Chemistry print out the job listing
	if re.search(r'\b(Chemistry)\b', dept.text):
		print("Chemistry job is found")
		print("Here is the position number : " + job.find_element(By.XPATH, "./td[1]").text)
		print("Here is the Job Title: " + job.find_element(By.XPATH, "./td[2]").text)
		print("Here is the Home Org/Dept.: " + dept.text)
		print("")
	i = i + 1

driver.save_screenshot('foundchemistry.png')
driver.quit()
