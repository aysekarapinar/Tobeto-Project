from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from constant import globalConstant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest



class Test_Chatbox:
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

    def find_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.click()

    def find_and_send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element.send_keys(value)

    def test_chatbox(self):
        sleep(5)
        chatbox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.chatBox)))
        chatbox.click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        symbol=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.symbolButton)))
        sleep(5)
        symbol.click()
        sleep(10)

    


    def test_chatbox_message(self):
        sleep(5)
        chatbox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.chatBox)))
        chatbox.click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        sleep(10)
        sendName=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.chatboxMessage)))
        sendName.send_keys("Mehmet Aslanbaş"+Keys.ENTER)
        sleep(10)
        chooseBox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.tobetoAbout)))
        chooseBox.click()
        sleep(10)


    def test_chatbox_finish(self):
        sleep(5)
        chatbox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.chatBox)))
        chatbox.click()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        messageIkon=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.messageFinish)))
        messageIkon.click()
        sleep(2)
        yesButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.yesButtonClick)))
        yesButton.click()
        sleep(2)
        # self.driver.switch_to.default_content()
        #emojiIkon=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emojiChoose)))
        #emojiIkon.click()
        #sleep(2)
        emojiMessageBox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.emojiBox)))
        emojiMessageBox.send_keys("Test edilmesi ne zor bir site!!!")
        sleep(2)
        surveyButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.surveyButton)))
        surveyButton.click()
        sleep(5)

    def test_emoji_control(self):
        sleep(5)
        chatbox=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.chatBox)))
        chatbox.click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        sleep(5)
        emojiButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.emojiButton)))
        emojiButton.click()
        #sleep(5)
        emojiClick=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,globalConstant.handButton)))
        emojiClick.click()
        sleep(5)
        addFileButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.addFile)))
        addFileButton.click()
        chooseFileButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,globalConstant.chooseFile)))
        chooseFileButton.click()
        sleep(10)
        