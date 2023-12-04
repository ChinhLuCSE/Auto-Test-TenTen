import time
import sys, os
from unittest import result
from dotenv import find_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"

url = "https://ten-ten.vercel.app/"
LOGIN_BUTTON_XPATH = "//a[contains(@href, 'https://school.moodledemo.net/login/index.php')]"
STUDENT_TEACHER_XPATH = (
    """//*[@id="region-main"]/div/div/div/div/div[3]/p[1]/a"""
)
LOUGOUT_BUTTON_XPATH = (
    "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]"
)
CHANGE_PASSWORD_LINK_XPATH = "//a[@href='https://account.hcmut.edu.vn/']"
CHANGE_PASSWORD_SUBMIT_XPATH = "//button[@type='submit']"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()


def goToLoginPage():
    driver.get(url)

class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()


class TestCreateLeaveRequest:
    @staticmethod
    def test(start_date, end_date, reason, expect, num):
        goToLoginPage()

        TestCreateLeaveRequest.login("024459868069", "123456")

        input_str = """start_date: %s
end_date: %s
reason: %s
""" % (
            start_date,
            end_date,
            reason,
        )
        TestUtil.makeSource(input_str, num)
        time.sleep(10)

        driver.find_element(By.XPATH, "//span[contains(.,'Leave Registration')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'+ Add leave')]").click()
        TestCreateLeaveRequest.fillform(start_date, end_date, reason)
        time.sleep(5)

        TestCreateLeaveRequest.check(SOL_DIR, num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")

        modal_title_ele = driver.find_element(By.XPATH, "//span[contains(.,'Application for leave')]")
        if modal_title_ele.is_displayed():
            dest.write("Failed")
            return
        dest.write("Successfully Create A Request")
        driver.get(url)
        driver.refresh()

    @staticmethod
    def fillform(start_date, end_date, reason):
        time.sleep(3)
        print(start_date)
        driver.find_element(By.XPATH, "//input[@value='']").send_keys(start_date, Keys.RETURN)
        # driver.find_element(By.XPATH, "//td[contains(@title, {start_date})]").send_keys(Keys.RETURN)
        driver.find_element(By.XPATH, "//input[@value='']").send_keys(end_date, Keys.RETURN)
        # driver.find_element(By.XPATH, "//td[contains(@title, {end_date})]").click()
        
        if len(reason) != 0:
            driver.find_element(By.XPATH, "//input[@type='text']").send_keys(reason)
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[contains(.,'Submit')]").click()
    
    @staticmethod
    def login(username, password):
        driver.find_element(By.ID, "phoneNumber").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "phoneNumber").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()