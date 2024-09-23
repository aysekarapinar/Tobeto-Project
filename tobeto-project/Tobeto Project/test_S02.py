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


class Test_Singup:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstant.URL)
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,globalConstant.singUp).click()
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

    
    def test_singup(self):
        # Kullanıcı bilgilerini doldurma
        self.input_text(By.XPATH, globalConstant.firstName, "pair4")
        self.input_text(By.NAME, globalConstant.lastName, "pair4")
        self.input_text(By.NAME, globalConstant.eposta, "pair4@gmail.com")
        self.input_text(By.XPATH, globalConstant.password, "123456")
        self.input_text(By.NAME, globalConstant.passwordAgain, "123456")

        # Kayıt olma butonuna tıklama
        self.click_element(By.XPATH, globalConstant.signUpButton)
        sleep(10)

        # Pop-up işlemleri
        self.click_element(By.XPATH, globalConstant.memberShipContract)
        self.click_element(By.XPATH, globalConstant.contract)
        self.click_element(By.XPATH, globalConstant.sendingEmail)
        self.click_element(By.XPATH, globalConstant.sendingPhone)

        # Telefon numarası girme ve devam etme
        self.input_text(By.ID, globalConstant.againPhone, "542 657 89 00")
        sleep(20)
        self.click_element(By.XPATH, globalConstant.continueButton)
        sleep(5)
    

    def test_perform_step(self, step):
        by, locator, action, value = step
        
        if action == "send_keys":
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
            element.clear()
            element.send_keys(value)
        elif action == "click":
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
            element.click()
        elif action == "sleep":
            sleep(value)
        elif action == "clear":
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
            element.clear()

    
    
    def test_phone_control(self):
        steps = [
            (By.XPATH, globalConstant.firstName, "send_keys", "Doğukan"),
            (By.NAME, globalConstant.lastName, "send_keys", "Arslan"),
            (By.NAME, globalConstant.eposta, "send_keys", "aaa97@gmail.com"),
            (By.NAME, globalConstant.password, "send_keys", "123456"),
            (By.NAME, globalConstant.passwordAgain, "send_keys", "123456"),
            (By.XPATH, globalConstant.signUpButton, "click", None),
            (None, None, "sleep", 10),
            (By.XPATH, globalConstant.memberShipContract, "click", None),
            (By.XPATH, globalConstant.contract, "click", None),
            (By.XPATH, globalConstant.sendingEmail, "click", None),
            (By.XPATH, globalConstant.sendingPhone, "click", None),
            (By.ID, globalConstant.againPhone, "send_keys", "535 898 23 6"),
            (None, None, "sleep", 10),
            (By.XPATH, globalConstant.continueButton, "click", None),
            (By.ID, globalConstant.againPhone, "clear", None),
            (By.ID, globalConstant.againPhone, "send_keys", "535 898 23 677"),
            (None, None, "sleep", 10),
            (By.XPATH, globalConstant.continueButton, "click", None),
            (By.ID, globalConstant.againPhone, "clear", None),
            (By.ID, globalConstant.againPhone, "send_keys", ""),
            (None, None, "sleep", 10),
            (By.ID, globalConstant.againPhone, "send_keys", "sıfırbeşyüz"),
            (By.XPATH, globalConstant.continueButton, "click", None)
        ]
        
        for step in steps:
            self.perform_step(step)
       


    def test_email_control(self):
        # E-posta alanına giriş ve temizleme işlemleri
        self.input_text(By.NAME, globalConstant.eposta, "e")
        sleep(5)  # İhtiyaç varsa bekleme süresi
        self.input_text(By.NAME, globalConstant.eposta, "")
        sleep(10)

    
    
    def test_registered_email(self):
        # Kayıt sayfasına git
        self.click_element(By.CSS_SELECTOR, globalConstant.singUp)
        sleep(5)
      

        # Formu doldur
        self.input_text(By.XPATH, globalConstant.firstName, "Özlem")
        self.input_text(By.NAME, globalConstant.lastName, "Akpınar")
        self.input_text(By.NAME, globalConstant.eposta, "ayseozlemkarapinar28@gmail.com")
        self.input_text(By.NAME, globalConstant.password, "123456")
        self.input_text(By.NAME, globalConstant.passwordAgain, "123456")

        # Kayıt ol
        self.click_element(By.XPATH, globalConstant.signUpButton)

        # Üyelik sözleşmesi ve diğer adımlar
        self.click_element(By.XPATH, globalConstant.memberShipContract)
        self.click_element(By.XPATH, globalConstant.contract)
        self.click_element(By.XPATH, globalConstant.sendingEmail)
        self.click_element(By.XPATH, globalConstant.sendingPhone)

        # Telefon numarası gir ve devam et
        self.input_text(By.ID, globalConstant.againPhone, "534 898 23 65")
        sleep(20)  # Bekleme süresi
        self.click_element(By.XPATH, globalConstant.continueButton)
        sleep(10)  # Bekleme süresi


   
   
    def test_password_control(self):
        # Formu doldur
        self.input_text(By.XPATH, globalConstant.firstName, "Özlem")
        self.input_text(By.NAME, globalConstant.lastName, "Akpınar")
        self.input_text(By.NAME, globalConstant.eposta, "ayseozlemkarapinar28@gmail.com")
        self.input_text(By.NAME, globalConstant.password, "12345")
        self.input_text(By.NAME, globalConstant.passwordAgain, "12345")

        # Kayıt ol
        self.click_element(By.XPATH, globalConstant.signUpButton)

        # Üyelik sözleşmesi ve diğer adımlar
        self.click_element(By.XPATH, globalConstant.memberShipContract)
        self.click_element(By.XPATH, globalConstant.contract)
        self.click_element(By.XPATH, globalConstant.sendingEmail)
        self.click_element(By.XPATH, globalConstant.sendingPhone)

        # Telefon numarası gir ve devam et
        self.input_text(By.ID, globalConstant.againPhone, "534 898 23 65")
        sleep(20)  # Bekleme süresi
        self.click_element(By.XPATH, globalConstant.continueButton)
        sleep(10)  # Bekleme süresi

    
    
    
    def test_password_again(self):
         # Formu doldur
        self.input_text(By.XPATH, globalConstant.firstName, "Özlem")
        self.input_text(By.NAME, globalConstant.lastName, "Akpınar")
        self.input_text(By.NAME, globalConstant.eposta, "ayseozlemkarapinar28@gmail.com")
        self.input_text(By.NAME, globalConstant.password, "12345")
        self.input_text(By.NAME, globalConstant.passwordAgain, "234567")

        # Kayıt ol
        self.click_element(By.XPATH, globalConstant.signUpButton)

        # Üyelik sözleşmesi ve diğer adımlar
        self.click_element(By.XPATH, globalConstant.memberShipContract)
        self.click_element(By.XPATH, globalConstant.contract)
        self.click_element(By.XPATH, globalConstant.sendingEmail)
        self.click_element(By.XPATH, globalConstant.sendingPhone)

        # Telefon numarası gir ve devam et
        self.input_text(By.ID, globalConstant.againPhone, "534 898 23 65")
        sleep(20)  # Bekleme süresi
        self.click_element(By.XPATH, globalConstant.continueButton)
        sleep(10)  # Bekleme süresi

    
    
    
    def test_password_error(self):
         # Formu doldur
        self.input_text(By.XPATH, globalConstant.firstName, "Özlem")
        self.input_text(By.NAME, globalConstant.lastName, "Akpınar")
        self.input_text(By.NAME, globalConstant.eposta, "ayseozlemkarapinar28@gmail.com")
        self.input_text(By.NAME, globalConstant.password, "123456")
        self.input_text(By.NAME, globalConstant.passwordAgain, "45678")

        # Kayıt ol
        self.click_element(By.XPATH, globalConstant.signUpButton)

        # Üyelik sözleşmesi ve diğer adımlar
        self.click_element(By.XPATH, globalConstant.memberShipContract)
        self.click_element(By.XPATH, globalConstant.contract)
        self.click_element(By.XPATH, globalConstant.sendingEmail)
        self.click_element(By.XPATH, globalConstant.sendingPhone)

        # Telefon numarası gir ve devam et
        self.input_text(By.ID, globalConstant.againPhone, "534 898 23 65")
        sleep(20)  # Bekleme süresi
        self.click_element(By.XPATH, globalConstant.continueButton)
        sleep(10)  # Bekleme süresi