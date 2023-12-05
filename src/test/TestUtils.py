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

driver = webdriver.Chrome()
# driver.maximize_window()
driver.set_window_size(1600, 1030)

def goToLoginPage():
    driver.get(url)

class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w", encoding="utf-8")
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


class TestUpdateEmployeeInfo:
    @staticmethod
    def test(name, gender, birth, address, expect, num):
        goToLoginPage()

        TestUpdateEmployeeInfo.login("0901235456", "123456")

        input_str = """name: %s
gender: %s
birth: %s
address: %s
""" % (
            name,
            gender,
            birth,
            address,
        )
        TestUtil.makeSource(input_str, num)
        time.sleep(10)

        driver.find_element(By.XPATH, "//span[contains(text(), 'Employee Management')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@id='2' and contains(text(), 'Update')]").click()
        TestUpdateEmployeeInfo.fillform(name, gender, birth, address)
        time.sleep(5)

        TestUpdateEmployeeInfo.check(SOL_DIR, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")

        warning = driver.find_element(By.XPATH, "//h1[contains(text(), 'Information')]")
        if warning.is_displayed():
            dest.write("Failed")
            return
        dest.write("Update successfully")
        driver.get(url)
        driver.refresh()

    @staticmethod
    def fillform(name, gender, birth, address):
        time.sleep(3)
        if len(name) != 0:
            namefield = driver.find_element(By.NAME, 'name')
            namefield.clear()
            namefield.click()
            if name != "empty":
                namefield.send_keys(name)
            else:
                namefield.send_keys(' \b')
        if len(gender) != 0:
            namefield = driver.find_element(By.NAME, 'gender')
            namefield.clear()
            namefield.click()
            if gender != "empty":
                namefield.send_keys(gender)
            else:
                namefield.send_keys(' \b')
        if len(birth) != 0:
            namefield = driver.find_element(By.NAME, 'birthDate')
            namefield.clear()
            namefield.click()
            if birth != "empty":
                namefield.send_keys(birth)
            else:
                namefield.send_keys(' \b')
        if len(address) != 0:
            namefield = driver.find_element(By.NAME, 'address')
            namefield.clear()
            namefield.click()
            if address != "empty":
                namefield.send_keys(address)
            else:
                namefield.send_keys(' \b')

        time.sleep(5)
        driver.find_element(By.XPATH, '//button[contains(text(),"Submit")]').click()

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