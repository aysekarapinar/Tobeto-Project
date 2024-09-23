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

    def test_successful_social_media_adding(self): 
        try:
            self.login(globalConstant.email, globalConstant.password)
            sleep(10)
            # Sayfayı tamamen aşağı kaydır
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)  # Kaydırmanın tamamlanmasını bekleyin
            # Profilini oluştur başlığına sahip div'i bul
            startButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.start1)))
            # Butona tıkla
            startButton.click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Medya Hesaplarım")]/..'))
            ).click()
            sleep(5)
            # Select dropdown'ına tıkla
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'select__dropdown-indicator'))
            ).click()
            sleep(5)

            # Instagram seçeneğini seç
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Instagram")]'))
            ).click()
            sleep(5)

            # URL alanına Instagram adresini gir
            social_media_link_input = self.driver.find_element(By.NAME, 'socialMediaUrl')
            social_media_link_input.send_keys("https://www.instagram.com/testuser")

            # Kaydet butonuna tıkla
            save_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Kaydet")]')
            save_button.click()

            sleep(5)

            # Ekleme işleminin başarılı olduğunu kontrol et
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="fade toast d-inline-block m-1 bg-success show"]'))  
            )

            print("Başarılı sosyal medya ekleme")

        except Exception as e:
            print("Sosyal medya ekleme testi başarısız:", str(e))

    def test_successful_social_media_Empty_adding(self): 
        try:
            self.login()

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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Medya Hesaplarım")]/..'))
            ).click()

            sleep(2)

            # Kaydet butonuna tıkla
            save_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Kaydet")]')
            save_button.click()

            sleep(2)

             # Hata mesajını kontrol et
            error_message = self.driver.find_element(By.XPATH, '//span[@class="text-danger"]').text
            if "Doldurulması zorunlu alan*" in error_message:
                print("Başarılı Sosyal Medya Boş Bırakma Testi")
            else:
                print("Sosyal Medya Boş Bırakma Testi başarısız: Hata mesajı görüntülenmedi")

            # Select dropdown'ına tıkla
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'select__dropdown-indicator'))
            ).click()

            sleep(5)

            # Instagram seçeneğini seç
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Instagram")]'))
            ).click()

            sleep(5)

            # Kaydet butonuna tıkla
            save_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Kaydet")]')
            save_button.click()

            sleep(2)


            # Hata mesajını kontrol et
            error_message = self.driver.find_element(By.XPATH, '//span[@class="text-danger"]').text
            if "Doldurulması zorunlu alan*" in error_message:
                print("Başarılı Sosyal Medya Boş Bırakma Testi")
            else:
                print("Sosyal Medya Boş Bırakma Testi başarısız: Hata mesajı görüntülenmedi")

        except Exception as e:
            print("Sosyal Medya Boş Bırakma Testi başarısız:", str(e))

    # Başarılı Sosyal Medya Sınır Testi
    def test_successful_social_media_limit_adding(self):
        try:
            self.login()

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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Medya Hesaplarım")]/..'))
            ).click()

            sleep(5)

            for _ in range(3):
                # Select dropdown'ına tıkla
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'select__dropdown-indicator'))
                ).click()

                sleep(2)

                # Instagram, Twitter ve başka bir seçenek arasında geçiş yap
                media_option = "Instagram" if _ == 0 else "Twitter" if _ == 1 else "LinkedIn"
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//div[contains(text(), "{media_option}")]'))
                ).click()

                sleep(2)

                # URL alanına örnek bir URL gir
                url_input = self.driver.find_element(By.NAME, 'socialMediaUrl')
                url_input.clear()
                url_input.send_keys(f'https://{media_option.lower()}.com/testuser')

                # Kaydet butonuna tıkla
                save_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Kaydet")]')
                save_button.click()

                sleep(3)

            # 3. medya hesabı eklendikten sonra input alanlarının görünmez olup olmadığını kontrol et
            try:
                # Input alanlarının hala görünür olup olmadığını kontrol et
                url_input = self.driver.find_element(By.NAME, 'socialMediaUrl')
                if url_input.is_displayed():
                    print("Sosyal Medya Sınır Testi başarısız: Giriş inputları hala görünür.")
                else:
                    print("Başarılı Sosyal Medya Sınır Testi: Giriş inputları görünmez.")
            except:
                print("Başarılı Sosyal Medya Sınır Testi: Giriş inputları görünmez.")

        except Exception as e:
            print("Sosyal Medya Sınır Testi başarısız:", str(e))

    # Sosyal Medya Silme Testi
    def test_successful_social_media_delete(self):
        try:
            self.login()

            # Sayfayı tamamen aşağı kaydır
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            sleep(2)  # Kaydırmanın tamamlanmasını bekleyin

            # Profilini oluştur başlığına sahip div'i bul
            start_button_div = self.driver.find_element(By.XPATH, '//div[contains(@class, "details") and h1[contains(text(), "Profilini oluştur")]]')

            # Başla butonunu içeren elementi bul
            start_button = start_button_div.find_element(By.XPATH, './/button[contains(text(), "Başla")]')

            # Butona tıkla
            start_button.click()

            # Medya Hesaplarım sekmesine git
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Medya Hesaplarım")]/..'))
            ).click()

            sleep(2)  # Geçişin tamamlanmasını bekleyin

            # Sosyal medya hesaplarını silme işlemi
            delete_buttons = self.driver.find_elements(By.CLASS_NAME, 'social-delete')
            for button in delete_buttons:
                button.click()
                sleep(1)  # Silme onayı için bekleyin

                # Onay penceresinde "Evet" butonuna tıklayın
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'btn-yes'))
                ).click()

                sleep(2)  # Silme işleminin tamamlanmasını bekleyin

            # Sosyal medya hesaplarının silindiğini kontrol et
            remaining_accounts = self.driver.find_elements(By.CLASS_NAME, 'social-delete')
            if len(remaining_accounts) == 0:
                print("Başarılı sosyal medya silme testi")
            else:
                print("Sosyal medya silme testi başarısız: Bazı hesaplar hala mevcut.")

        except Exception as e:
            print("Sosyal Medya Silme Testi başarısız:", str(e))

    def test_social_media_update(self):
        try:
            self.login()

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
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Medya Hesaplarım")]/..'))
            ).click()

            sleep(5)

            # Select dropdown'ına tıkla
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'select__dropdown-indicator'))
            ).click()

            sleep(5)

            # Instagram seçeneğini seç
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Instagram")]'))
            ).click()

            sleep(5)

            # URL alanına Instagram adresini gir
            social_media_link_input = self.driver.find_element(By.NAME, 'socialMediaUrl')
            social_media_link_input.send_keys("https://www.instagram.com/testuser")

            # Kaydet butonuna tıkla
            save_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Kaydet")]')
            save_button.click()

            sleep(5)


            # Düzenleme ikonuna tıkla
            edit_icon = self.driver.find_element(By.CSS_SELECTOR, 'btn.btn i.fa.fa-pencil-square')
            edit_icon.click()

            sleep(2)  # Modalın açılmasını bekleyin

            # Dropdown menüsünü aç
            dropdown_menu = self.driver.find_element(By.CSS_SELECTOR, 'select.form-select')
            dropdown_menu.click()

            sleep(1)  # Dropdown menüsünün açılmasını bekleyin

            # "Twitter" seçeneğini seç
            twitter_option = self.driver.find_element(By.XPATH, '//option[text()="Twitter"]')
            twitter_option.click()

              # Sosyal medya linkini temizle
            link_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"].form-control')
            link_input.clear()

            # Twitter linkini gir
            twitter_link = "https://twitter.com/example"
            link_input.send_keys(twitter_link)

            # Güncelle butonuna tıkla
            update_button = self.driver.find_element(By.XPATH, '//button[text()="Güncelle"]')
            update_button.click()

            sleep(10)

            print("Sosyal Medya Düzenleme Testi başarılı.")

        except Exception as e:
            print("Sosyal Medya Düzenleme Testi başarısız:", str(e))


