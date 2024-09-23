from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from constant import globalConstant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import openpyxl


class Test_Forgot_Password:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstant.URL)
        sleep(5)
        
    
    def teardown_method(self):
        self.driver.quit()


    def input_text(self, by, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def click_element(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def find_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.click()

    def find_and_send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element.send_keys(value)

    def test_forgot_password(self):
        sleep(2)
        forgotPassword=self.driver.find_element(By.XPATH, globalConstant.forgotPasswordButton)
        actions = ActionChains(self.driver)
        actions.move_to_element(forgotPassword).perform()
        sleep(5)
        forgotPassword.click()
        passwordReset=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.passwordResetBox)))
        passwordReset.send_keys("ayseozlemkarapinar28@gmail.com")
        send=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.sendButton)))
        send.click()
        sleep(5)


    def test_incorrect_email_request(self):
        sleep(2)
        forgotPassword=self.driver.find_element(By.XPATH, globalConstant.forgotPasswordButton)
        actions = ActionChains(self.driver)
        actions.move_to_element(forgotPassword).perform()
        sleep(5)
        forgotPassword.click()
        passwordReset=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.passwordResetBox)))
        passwordReset.send_keys("ayseozlemkarapinar")
        send=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.sendButton)))
        send.click()
        sleep(5)

    