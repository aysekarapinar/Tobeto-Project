from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from constant import globalConstant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest


class Test_S18:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstant.URL)
        sleep(5)
    
    def teardown_method(self):
        self.driver.quit()

    def login(self, email, password):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, globalConstant.emailBox))
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, globalConstant.passwordBox))
        )
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, globalConstant.loginButton))
        )
        login_button.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="fade toast d-inline-block m-1 bg-success show"]'))  
            )
            print("Başarılı giriş")
        except:
            print("Giriş başarısız")
            
            sleep(3)

    def test_successful_language_adding(self): 
        try:
            self.login(globalConstant.email, globalConstant.password)
            sleep(10)
            # Sayfayı tamamen aşağı kaydır
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)  # Kaydırmanın tamamlanmasını bekleyin

            # Profilini oluştur başlığına sahip div'i bul
            start_button_div = self.driver.find_element(By.XPATH, '//div[contains(@class, "details") and h1[contains(text(), "Profilini oluştur")]]')

            # Başla butonunu içeren elementi bul
            start_button = start_button_div.find_element(By.XPATH, './/button[contains(text(), "Başla")]')

            # Butona tıkla
            start_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Yabancı Dillerim")]/..'))
            ).click()

            sleep(5)

            # İlk dropdown'a tıklama işlemi ve "Arapça"yı seçme
            first_dropdown = self.driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
            first_dropdown.click()

            # "Arapça" seçeneğini tıkla
            arabic_option = self.driver.find_element(By.XPATH, '//div[@class="select__option" and contains(text(), "Arapça")]')
            arabic_option.click()

            print("Arapça seçildi")

            # İkinci dropdown'a tıklama işlemi ve "Temel Seviye (A1, A2)"yi seçme
            second_dropdown = self.driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
            second_dropdown.click()

            # "Temel Seviye (A1, A2)" seçeneğini tıkla
            basic_level_option = self.driver.find_element(By.XPATH, '//div[@class="select__option" and contains(text(), "Temel Seviye (A1, A2)")]')
            basic_level_option.click()

            print("Temel Seviye (A1, A2) seçildi")

            sleep(2)  # Seçimin tamamlanmasını bekleyin

            # Kaydet butonuna tıkla
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Kaydet")]'))
            ).click()

            print("Başarılı Dil Ekleme")

        except Exception as e:
            print("Dil ekleme testi başarısız:", str(e))
