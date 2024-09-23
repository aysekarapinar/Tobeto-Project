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


class Test_Announcement_News:
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
    

    def test8_ac1(self):
        self.login()
        sleep(20)
        # Hoşgeldiniz panelinde scroll'u aşağı kaydır
        sleep(2)  # Sayfanın tamamen yüklenmesi için bekleme süresi
        self.driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
        newsButton= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,globalConstant.news)))
        actions = ActionChains(self.driver)
        actions.move_to_element(newsButton).perform()
        newsButton.click()

    def test8_ac2(self):
        self.login()
        sleep(20) 
        newsButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,globalConstant.news)))
        actions = ActionChains(self.driver)
        actions.move_to_element(newsButton).perform()
        newsButton.click()
        sleep(3)
        show_more_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,globalConstant.newsShowMore)))
        actions = ActionChains(self.driver)
        actions.move_to_element(show_more_button).perform()
        show_more_button.click()
        sleep(3)
        search_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "search")))
        search_box.clear()
        search_box.send_keys("ocak ayı")
        search_box.send_keys(Keys.RETURN)
        search_box.clear()
        search_box.send_keys("ocak ayı toplandı")
        search_box.send_keys(Keys.RETURN)
        tür_dropdown = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/div[2]/div/div/div[2]/button")))
        tür_dropdown.click()
        sleep(2)
        duyuru_seçeneği = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//label[text()='Duyuru']")))
        duyuru_seçeneği.click()
        sleep(2)

       

