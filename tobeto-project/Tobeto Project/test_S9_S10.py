from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from constant import globalConstant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest


class Test_S9_S10:
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


    def login(self):
        emailInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emailBox)))
        emailInput.send_keys(globalConstant.email)
        passwordInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.passwordBox)))
        passwordInput.send_keys(globalConstant.password)
        sleep(60)
        loginInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.loginButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginInput).perform()
        loginInput.click()
        sleep(30)
    

    def test_S9_C1_C2(self):
        self.login()
        self.click_element(By.XPATH,globalConstant.profilButton)
        self.click_element(By.XPATH,globalConstant.edit)
        sleep(5)
        self.driver.back()
        self.click_element(By.XPATH, globalConstant.share)
        self.click_element(By.XPATH, globalConstant.dropDown)
        self.click_element(By.XPATH, globalConstant.dropDown)
        self.click_element(By.XPATH,globalConstant.copyLink)

    def test_S9_C3(self):
        self.login()
        self.click_element(By.XPATH,globalConstant.profilButton)
        sleep(5)
        self.driver.execute_script("window.scrollTo(0,907.2000122070312)")
        self.click_element(By.XPATH,globalConstant.certificate)
        sleep(5)

    def test_S9_C4(self):
        self.login()
        self.click_element(By.XPATH,globalConstant.profilButton)
        sleep(5)
        self.click_element(By.CSS_SELECTOR,globalConstant.socialMedia)
        sleep(5)

    def test_S9_C5_C6(self):
        self.login()
        self.click_element(By.XPATH,globalConstant.profilButton)
        sleep(5)
        self.click_element(By.CSS_SELECTOR,globalConstant.seeIkon)
        sleep(5)

    def test_S10_C1_C2(self):
        self.login()
        self.click_element(By.XPATH,globalConstant.reviews)
        self.click_element(By.XPATH,globalConstant.viewReport)
        sleep(5)

    def test_S10_C3(self):
        self.login()
        self.click_element(By.CSS_SELECTOR,globalConstant.rating)
        self.click_element(By.XPATH,globalConstant.report2)
        sleep(5)
        self.click_element(By.XPATH,globalConstant.report3)
        sleep(5)











