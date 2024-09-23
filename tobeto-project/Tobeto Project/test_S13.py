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

    def test_S13_C1(self):
        self.login()
        startButon=self.driver.find_element(By.XPATH,globalConstant.startButton12XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(startButon).perform()
        sleep(7)
        startButon.click()
        sleep(5)
        name=self.driver.find_element(By.XPATH,globalConstant.nameXPATH)
        name.clear()
        sleep(3)
        name.send_keys("osman")
        lastname=self.driver.find_element(By.XPATH,globalConstant.lastnameXPATH)
        lastname.clear()
        sleep(3)
        lastname.send_keys("arslan")
        phone=self.driver.find_element(By.XPATH,globalConstant.phoneNumberXPATH)
        phone.clear()
        sleep(5)
        phone.send_keys("")
        id=self.driver.find_element(By.XPATH,globalConstant.idXPATH)
        id.clear()
        sleep(5)
        id.send_keys("14476033042")
        sleep(5)
        adress=self.driver.find_element(By.XPATH,globalConstant.addressXPATH)
        adress.clear()
        sleep(10)
        adress.send_keys("Atatürk Mahallesi,İstiklal Sokak No:1923")
        sleep(5)
        test=self.driver.find_element(By.XPATH,globalConstant.textXPATH)
        test.clear()
        sleep(5)
        test.send_keys("yazılım kalite test")
        sleep(10)
        saveButton=self.driver.find_element(By.XPATH,globalConstant.saveXPATH) 
        actions = ActionChains(self.driver)
        actions.move_to_element(saveButton).perform()
        sleep(7)
        saveButton.click()

    def test_S13_C2(self):
        self.login()
        sleep(10)
        startButon=self.driver.find_element(By.XPATH,globalConstant.startButton12XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(startButon).perform()
        sleep(7)
        startButon.click()
        sleep(5)
        image=self.driver.find_element(By.XPATH,globalConstant.profillXPATH)
        image.click()
        sleep(2)
        searchButton=self.driver.find_element(By.XPATH,globalConstant.searchXPATH)
        searchButton.click()
        sleep(20)

    def test_S13_C3(self):
        self.login()
        sleep(10)
        startButon=self.driver.find_element(By.XPATH,globalConstant.startButton12XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(startButon).perform()
        sleep(7)
        startButon.click()
        sleep(5)
        id=self.driver.find_element(By.XPATH,globalConstant.idXPATH)
        id.clear()
        sleep(2)
        id.send_keys("1447523323222")  #11 hane girilebiliyor fazla karaktere izin verilmiyor
        sleep(3)

    def test_S13_C4(self):
        self.login()
        sleep(10)
        startButon=self.driver.find_element(By.XPATH,globalConstant.startButton12XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(startButon).perform()
        sleep(7)
        startButon.click()
        sleep(5)
        id=self.driver.find_element(By.XPATH,globalConstant.idXPATH)
        id.clear()
        sleep(2)
        saveButton=self.driver.find_element(By.XPATH,globalConstant.saveXPATH)  
        actions = ActionChains(self.driver)
        actions.move_to_element(saveButton).perform()
        sleep(7)
        saveButton.click()
        sleep(5)
        erMassage=self.driver.find_element(By.XPATH, globalConstant.erMassageXPATH) 
        assert erMassage.text=="Satın alınan eğitimlerin faturası için doldurulması zorunlu alan."

    def test_S13_C5(self):
        self.login()
        sleep(10)
        startButon=self.driver.find_element(By.XPATH,globalConstant.startButton12XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(startButon).perform()
        sleep(7)
        startButon.click()
        sleep(5)
        addres=self.driver.find_element(By.XPATH,globalConstant.addressXPATH)
        addres.clear()
        sleep(5)
        addres.send_keys("Feridun Çelik Mahallesi,1722.sokakadssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        sleep(5)
        test=self.driver.find_element(By.XPATH,globalConstant.textXPATH)
        test.clear()
        sleep(5)
        test.send_keys("bensssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        sleep(5)
        saveButton=self.driver.find_element(By.XPATH,globalConstant.saveXPATH) 
        actions = ActionChains(self.driver)
        actions.move_to_element(saveButton).perform()
        sleep(7)
        saveButton.click()
        sleep(10)
        alertMas=self.driver.find_element(By.XPATH,globalConstant.alertXPATH)
        assert alertMas.text=="En fazla 200 karakter girebilirsiniz"
        sleep(5)
        alertMass=self.driver.find_element(By.XPATH,globalConstant.alertXPATH2)
        assert alertMass.text=="En fazla 300 karakter girebilirsiniz"