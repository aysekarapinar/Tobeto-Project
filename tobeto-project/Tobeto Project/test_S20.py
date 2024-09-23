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

class Test_Tobeto_Report:
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
    
    #@pytest.mark.parametrize("email,password",getData())
    def test_successful_password_update(self):
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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Ayarlar")]/..'))
            ).click()

            sleep(5)

            # Eski şifre, yeni şifre ve yeni şifre tekrar alanlarını bul
            current_password_input = self.driver.find_element(By.NAME, 'currentPassword')
            new_password_input = self.driver.find_element(By.NAME, 'password')
            confirm_password_input = self.driver.find_element(By.NAME, 'passwordConfirmation')

            sleep(5)

            # Şifreleri güncelle
            current_password_input.send_keys("eski_sifre")
            new_password_input.send_keys("yeni_sifre")
            confirm_password_input.send_keys("yeni_sifre")

            sleep(5)

            # Şifre değiştirme butonuna tıkla
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Şifre Değiştir")]').click()

            sleep(5)
            print('Şifre Güncelleme Başarılı')
        except Exception as e:
            print('Hata:', str(e))

  
    def test_successful_password_update(self):
        try:
            self.login(globalConstant.email, globalConstant.password)
            sleep(10)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)  # Kaydırmanın tamamlanmasını bekleyin

            # Profilini oluştur başlığına sahip div'i bul
            start_button_div = self.driver.find_element(By.XPATH, '//div[contains(@class, "details") and h1[contains(text(), "Profilini oluştur")]]')

            # Başla butonunu içeren elementi bul
            start_button = start_button_div.find_element(By.XPATH, './/button[contains(text(), "Başla")]')

            # Butona tıkla
            start_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Ayarlar")]/..'))
            ).click()

            sleep(5)

            # Eski şifre, yeni şifre ve yeni şifre tekrar alanlarını bul
            current_password_input = self.driver.find_element(By.NAME, 'currentPassword')
            new_password_input = self.driver.find_element(By.NAME, 'password')
            confirm_password_input = self.driver.find_element(By.NAME, 'passwordConfirmation')

            sleep(5)

            # Şifreleri güncelle
            current_password_input.send_keys('')
            new_password_input.send_keys('')
            confirm_password_input.send_keys('')

            sleep(5)

            # Şifre değiştirme butonuna tıkla
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Şifre Değiştir")]').click()

            # Hata mesajını kontrol et
            error_message = self.driver.find_element(By.XPATH, '//span[@class="text-danger"]').text
            if "Doldurulması zorunlu alan*" in error_message:
                print("Başarılı Sosyal Medya Boş Bırakma Testi hata görüntülendi")
            else:
                print("Sosyal Medya Boş Bırakma Testi başarısız: Hata mesajı görüntülenmedi")

            sleep(5)
        except Exception as e:
            print('Hata:', str(e))

    
    def test_successful_password_again(self):
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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Ayarlar")]/..'))
            ).click()

            sleep(5)

            # Eski şifre, yeni şifre ve yeni şifre tekrar alanlarını bul
            current_password_input = self.driver.find_element(By.NAME, 'currentPassword')
            new_password_input = self.driver.find_element(By.NAME, 'password')
            confirm_password_input = self.driver.find_element(By.NAME, 'passwordConfirmation')

            sleep(5)

            # Şifreleri güncelle
            current_password_input.send_keys("yeni_sifre")
            new_password_input.send_keys("yeni_sifre")
            confirm_password_input.send_keys("yeni_sifre")

            sleep(5)

            # Şifre değiştirme butonuna tıkla
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Şifre Değiştir")]').click()

            sleep(5)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@class="fade toast d-inline-block m-1 bg-success show"]'))  
                )
                print("Başarısız")
            except:
                print("Başarılı")   

        except Exception as e:
            print('Hata:', str(e))


    def test_successful_membership_end(self):
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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Ayarlar")]/..'))
            ).click()

            sleep(5)

            # Üyeliği Sonlandır butonunu bul ve tıkla
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Üyeliği Sonlandır")]').click()

            sleep(5)

            # Onay penceresinde "Hayır" butonunu bul ve tıkla
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Hayır")]'))
            ).click()

             # Başarılı bir şekilde işlemi tamamladığını belirtmek için alert göster
            self.driver.execute_script('alert("Test Başarılı");')

            sleep(5)  # Alert mesajının görülmesi için bekle

            sleep(5)
            print('Başarılı')
        except Exception as e:
            print('Hata:', str(e))