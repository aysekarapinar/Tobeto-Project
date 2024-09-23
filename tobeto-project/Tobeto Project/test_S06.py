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


class Test_Welcome_Panel:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstant.URL)
        sleep(5)
        
    
    def teardown_method(self):
        self.driver.quit()


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
        sleep(5)

    
    def click_element(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()

  

    def test_panel_control(self):
        emailInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emailBox)))
        emailInput.send_keys(globalConstant.email)
        passwordInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.passwordBox)))
        passwordInput.send_keys(globalConstant.password)
        sleep(50)
        loginInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.loginButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginInput).perform()
        loginInput.click()
        sleep(5)
        lessons=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.lessonsButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(lessons).perform()
        lessons.click()
        sleep(5)
        notificaton=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.notificatonButton)))
        notificaton.click()
        sleep(5)
        surveyTab=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.surveyButton)))
        surveyTab.click()
        sleep(5)
        examName=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.examName)))
        examName.click()
        sleep(5)
        report=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.report)))
        actions = ActionChains(self.driver)
        actions.move_to_element(report).perform()
        report.click()
        sleep(5)
        close=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.closeButton)))
        close.click()
        sleep(5)



    def test_personalspace_control(self):
        self.login()
        profil=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.start1)))
        actions = ActionChains(self.driver)
        actions.move_to_element(profil).perform()
        profil.click()
        sleep(5)
        self.driver.back()
        sleep(5)
        evaluateYourself=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.start2)))
        actions = ActionChains(self.driver)
        actions.move_to_element(evaluateYourself).perform()
        evaluateYourself.click()
        sleep(5)
        self.driver.back()
        sleep(5)
        startingLearning=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.start3)))
        startingLearning.click()
        sleep(5)


    def test_personalspace_control2(self):
    # Kullanıcı girişi yapılıyor
      self.login()
       # Login işlemi için yeterli zaman tanıyoruz
    
    # Profil butonuna tıklama işlemi
      self.click_element(globalConstant.start1)
      self.driver.back()
      sleep(5)
    
    # Kendi kendini değerlendirme butonuna tıklama işlemi
      self.click_element(globalConstant.start2)
      self.driver.back()
      sleep(5)
    
    # Öğrenmeye başlama butonuna tıklama işlemi
      self.click_element(globalConstant.start3)
      sleep(5)

    def click_element(self, xpath):
        """Belirtilen XPATH'e sahip elemente tıklar."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        sleep(5)