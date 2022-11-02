import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'
URL2 = 'https://www.saucedemo.com/inventory.html'

class Test1:
    @pytest.fixture()
    def setup(self):
        chrome_driver = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_driver)
        self.driver.get(URL)

    def test_click_login_btn(self, setup, test_login, tear_down):
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()

        assert self.driver.current_url == URL2, 'Página incorreta!'

        # error_msg = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        # assert error_msg == 'Epic sadface: Username is required', 'Mensagem de erro não encontrada!'

        #time.sleep(3)

    @pytest.fixture()
    def test_login(self):
        user_login =  self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        user_password = self.driver.find_element(By.ID,'password').send_keys('secret_sauce')



    @pytest.fixture()
    def tear_down(self):
        yield
        self.driver.quit()
