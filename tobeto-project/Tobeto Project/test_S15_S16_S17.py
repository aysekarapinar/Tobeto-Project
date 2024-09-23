from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from constant import globalConstant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

class Test_Tobeto_Report:
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
        sleep(30)
        loginInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.loginButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginInput).perform()
        loginInput.click()

    def test_S15(self):
            self.login()
            sleep(10)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(5)
            educationbutton=self.driver.find_element(By.CLASS_NAME,globalConstant.educationXPATH)
            educationbutton.click()
            sleep(5)
            educationalbackground=self.driver.find_element(By.XPATH,globalConstant.educationalbackgroundXPATH)
            educationalbackground.click()
            sleep(5)
            dropdown = self.driver.find_element(By.CLASS_NAME,globalConstant.dropdownXPATH)
            dropdown.click()
            sleep(1)
            lisans_option = self.driver.find_element(By.XPATH, '//div[contains(@class, "select__option") and text()="Lisans"]')
            lisans_option.click()
            sleep(1)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, "University")))
            self.driver.find_element(By.NAME, "University").send_keys("Erzincan Üniversitesi")
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, "Department")))
            self.driver.find_element(By.NAME, "Department").send_keys("Yazılım")
            starting_year=self.driver.find_element(By.XPATH, "/html/body/div/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input").click()
            self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div[2]/div/div").click()
            self.driver.find_element(By.XPATH, "/html/body/div/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input").click()
            self.driver.find_element(By.XPATH, "//div[2]/div/div[4]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
            self.driver.find_element(By.XPATH, "//div/div/div/div/div[2]").text == "• Eğitim bilgisi eklendi."
            sleep(15)

    
    def test_S16(self):
            self.login()
            sleep(10)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(3)
            yetkinliklerim=self.driver.find_element(By.XPATH,globalConstant.yetkinliklerimXPATH)
            yetkinliklerim.click()
            sleep(3)
            yetenek=self.driver.find_element(By.XPATH,globalConstant.yetenekXPATH)
            yetenek.click()
            sleep(3)
            savebutton=self.driver.find_element(By.XPATH,globalConstant.saveXPATH)
            savebutton.click()
            sleep(3)
            message=self.driver.find_element(By.XPATH,globalConstant.messageXPATH)
            assert message.text == '• Yetenek eklendi.'
            sleep(3)

    
    def test_S16_C2(self):
            self.login()
            sleep(10)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(3)
            yetkinliklerim=self.driver.find_element(By.XPATH,globalConstant.yetkinliklerimXPATH)
            yetkinliklerim.click()
            sleep(3)
            savebutton=self.driver.find_element(By.XPATH,globalConstant.saveXPATH)
            savebutton.click()
            sleep(3)
            message2=self.driver.find_element(By.XPATH,globalConstant.message2XPATH)
            assert message2.text == '• Herhangi bir yetenek seçmediniz!'
            sleep(3)

    
    def test_S16_C3(self):
            self.login()
            sleep(10)
            sleep(3)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(3)
            yetkinliklerim=self.driver.find_element(By.XPATH,globalConstant.yetkinliklerimXPATH)
            yetkinliklerim.click()
            sleep(3)
            delete=self.driver.find_element(By.XPATH,globalConstant.deleteXPATH)
            delete.click()
            sleep(3)
            yes=self.driver.find_element(By.XPATH,globalConstant.yesXPATH)
            yes.click()
            sleep(3)
            message3=self.driver.find_element(By.XPATH,globalConstant.message3XPATH)
            assert message3.text == '• Yetenek kaldırıldı.'
            sleep(3)

    
    def test_S17(self):
            self.login()
            sleep(10)
            sleep(3)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(3)
            sertifikalarım=self.driver.find_element(By.XPATH,globalConstant.sertifikalarımXPATH)
            sertifikalarım.click()
            sleep(3)
            sertifika=self.driver.find_element(By.XPATH,globalConstant.sertifikaXPATH)
            sertifika.send_keys("Yazılım Sertifikam")
            sleep(3)
            tarih=self.driver.find_element(By.XPATH,globalConstant.tarihXPATH)
            tarih.send_keys("2024")
            sleep(3)
            gozat=self.driver.find_element(By.XPATH,globalConstant.gozatXPATH)
            gozat.click()
            sleep(3)

    
    def test_S17_C3(self):
            self.login()
            sleep(10)
            sleep(3)
            profilbutton=self.driver.find_element(By.XPATH,globalConstant.profilXPATH)
            actions = ActionChains(self.driver)
            actions.move_to_element(profilbutton).perform()
            profilbutton.click()
            sleep(3)
            sertifikalarım=self.driver.find_element(By.XPATH,globalConstant.sertifikalarımXPATH)
            sertifikalarım.click()
            sleep(3)
            delete2=self.driver.find_element(By.XPATH,globalConstant.delete2XPATH)
            delete2.click()
            sleep(3)
            yes2=self.driver.find_element(By.XPATH,globalConstant.yes2XPATH)
            yes2.click()
            sleep(3)
            message4=self.driver.find_element(By.XPATH,globalConstant.message4XPATH)
            assert message4.text == '• Dosya kaldırma işlemi başarılı.'
            sleep(3)