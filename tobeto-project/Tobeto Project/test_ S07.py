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


class Test_Training_Panel:
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
        sleep(20)
        loginInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.loginButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginInput).perform()
        loginInput.click()
        sleep(5)

    def test_training_panel(self):
        emailInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emailBox)))
        emailInput.send_keys(globalConstant.email)
        passwordInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.passwordBox)))
        passwordInput.send_keys(globalConstant.password)
        sleep(15)
        loginInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.loginButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginInput).perform()
        loginInput.click()
        lessons=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.lessonsButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(lessons).perform()
        lessons.click()
        sleep(5)
        showMore=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.showMoreButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(showMore).perform()
        showMore.click()
        sleep(5)
        goToTraining=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.goTo)))
        actions = ActionChains(self.driver)
        actions.move_to_element(goToTraining).perform()
        goToTraining.click()
        sleep(5)


    def test_contect_control(self):
        emailInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emailBox)))
        emailInput.send_keys(globalConstant.email)
        passwordInput=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.passwordBox)))
        passwordInput.send_keys(globalConstant.password)
        sleep(20)
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
        educationButton=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.education)))
        actions = ActionChains(self.driver)
        actions.move_to_element(educationButton).perform()
        educationButton.click()
        sleep(20)
        favorite=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.addFavorite)))
        sleep(20)
        favorite.click()
        like=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.likeButton)))
        like.click()
        sleep(5)
        about=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.aboutButton)))
        about.click()
        contect=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.contectButton)))
        contect.click()
        detail=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.detailButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(detail).perform()
        detail.click()
        sleep(5)
        goToLesson=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.goToLesson)))
        goToLesson.click()
        sleep(2)
        detail=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.detailButton)))
        detail.click()
        x=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.xButton)))
        x.click()
        sleep(5)

    def test_search_education(self):
        self.login()
        sleep(30)
        lessons=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.lessonsButton)))
        actions = ActionChains(self.driver)
        actions.move_to_element(lessons).perform()
        lessons.click()
        sleep(5)
        showMore=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.showMoreButton)))
        showMore.click()
        search=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.searchBox)))
        search.send_keys("Dr.Ecmel Ayral’dan Hoşgeldin Mesajı")
        listBox=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, globalConstant.listButton)))
        listBox.click()
        #searchList=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.searchList))).click()
        #searchList.send_keys("İstanbul Kodluyor")
        alphabetList=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.alphabetListButton)))
        alphabetList.click()


    