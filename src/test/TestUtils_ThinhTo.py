from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

import unittest
import time


TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"

base_url = "https://ten-ten-v2.vercel.app/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)


def signIn(username, password):
	time.sleep(20)
	driver.get(base_url + "sign-in")

	# find and fill info
	username_input = driver.find_element(By.XPATH, '//input[@id="phoneNumber"]')
	password_input = driver.find_element(By.XPATH, '//input[@id="password"]')

	username_input.send_keys(username)
	password_input.send_keys(password)

	# find term of service and accept
	tos_check_label = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/form/div[3]/div[1]/label')
	tos_check_label.click()

	# find login button and click
	login_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/form/button')
	login_button.click()

	# make sure logged in
	welcome_h1 = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/h1')
	time.sleep(20)


# logout
def logOut():
	time.sleep(20)
	logout_btn = driver.find_element(By.XPATH, '//aside[@id="default-sidebar"]/div/div/a[@href="/sign-in"]')
	logout_btn.click()
	time.sleep(20)


# navigate to statistic and return pipeline ([], [])
def getStatistic(status_month="1", dayoff_month="1"):
	time.sleep(20)
	driver.get(base_url + "manage/statistic")
	time.sleep(20)

	# status section
	# time.sleep(3)
	# wait for data to fetch
	dummy_first_block_dayoff = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[2]/div[1]')
	select_status = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/section[1]/select')
	drop_status = Select(select_status)
	drop_status.select_by_value(status_month)

	time.sleep(20)
	select_dayoff = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/select')
	drop_dayoff = Select(select_dayoff)
	drop_dayoff.select_by_value(dayoff_month)

	# refetch data
	time.sleep(4)

	pending_status = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/section[2]/div[1]/div[1]')
	# print(pending_status.text)

	approved_status = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/section[2]/div[2]/div[1]')
	# print(approved_status.text)

	rejected_status = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/section[2]/div[3]/div[1]')
	# print(rejected_status.text)

	combined_status = {
		"pending": int(pending_status.text),
		"approved": int(approved_status.text),
		"rejected": int(rejected_status.text),
	}

	# dayoff section
	dayoff_count = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[2]/div/div[1]')
	dayoff_name = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[2]/div/div[3]')
	dayoff_dict = {
		name.text: int(count.text) for (name, count) in zip(dayoff_name, dayoff_count)
	}

	# combine 2 sections
	statistic = {
		"status": combined_status,
		"dayoff": dayoff_dict
	}

	return statistic


def addLeave(begin="2023-12-01", end="2023-12-04"):
	driver.get(base_url + "leave-registration")

	# wait fetch data
	time.sleep(10)

	add_leave_btn = driver.find_element(By.XPATH, '/html/body/div/div/button')
	add_leave_btn.click()

	date_pickers = driver.find_elements(By.CSS_SELECTOR, 'div.ant-picker> div.ant-picker-input > input')
	date_pickers[0].send_keys(begin)
	date_pickers[1].send_keys(end)

	reason_field = driver.find_element(By.XPATH, '//input[@type="text"]')
	reason_field.send_keys("auto reason - Thinh To testcase")

	submit_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/form/div[5]/button')
	submit_btn.click()
	time.sleep(10)


def getInfo():
	employee_name = driver.find_element(By.CSS_SELECTOR, "body > div > div.flex.flex-col.items-center.justify-center > div.flex.w-full.flex-col.items-center.p-2.mt-14 > span.font-bold")
	while employee_name.text == "Loading...":
		time.sleep(0.5)
		employee_name = driver.find_element(By.CSS_SELECTOR,
								   "body > div > div.flex.flex-col.items-center.justify-center > div.flex.w-full.flex-col.items-center.p-2.mt-14 > span.font-bold")
	employee_id = driver.find_element(By.CSS_SELECTOR, "body > div > div.flex.flex-col.items-center.justify-center > div.flex.w-full.flex-col.items-center.p-2.mt-14 > span:nth-child(4)")
	return employee_name.text + ' ' + employee_id.text.replace('ID', 'id', 1)
	time.sleep(20)


def approvedRequest(approved=1):
	time.sleep(20)
	driver.get(base_url + 'manage/leave')
	time.sleep(20)

	pagination_btns = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div/div/ul/li/a')[::-1]
	for pagination_btn in pagination_btns:
		try:
			pagination_btn.click()
			time.sleep(20)
			approve_btns = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr/td[8]/div/div[1]/button')
			if not approve_btns:
				continue
			reject_btns = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr/td[8]/div/div[2]/button')
			last_approve_btn = approve_btns[-1]
			last_reject_btn = reject_btns[-1]

			if approved == 1:
				time.sleep(20)
				last_approve_btn.click()
				time.sleep(20)
				driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/button[2]').click()
				time.sleep(20)
				break
			elif approved == 2:
				time.sleep(20)
				last_reject_btn.click()
				time.sleep(20)
				driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/button[2]').click()
				time.sleep(20)
				break

		except NoSuchElementException:
			pass




class TestStatistic:
	@staticmethod
	def mainFlow(approved=0, status_month="1", dayoff_month="1", start_date="2023-12-01", end_date="2023-12-01",
				expected_status=1, expected_dayoff=0):
		# Get the old data in admin
		signIn("0901235456", "123456")
		getInfo()
		old_statistic = getStatistic(status_month, dayoff_month)
		# logOut()

		# Generate new Data
		signIn("026503754569", "123456")
		info = getInfo()
		# addLeave(start_date, end_date)
		# logOut()

		# Check new Data
		signIn("023674880804", "123456")
		getInfo()
		if approved == 1 or approved == 2:
			approvedRequest(approved)
		new_statistic = getStatistic(status_month, dayoff_month)

		# assert status
		if approved == 0:
			update_status = "pending"
		elif approved == 1:
			update_status = "approved"
		elif approved == 2:
			update_status = "rejected"
		else:
			return

		assert_status = old_statistic["status"][update_status] + expected_status == new_statistic["status"][update_status]
		print(old_statistic)
		print(new_statistic)

		# assert dayoff
		assert_dayoff = old_statistic["dayoff"][info] + expected_dayoff == new_statistic["dayoff"][info]
		return assert_status, assert_dayoff
