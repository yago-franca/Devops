import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL2 = 'https://www.saucedemo.com/inventory.html'
URL = "https://www.saucedemo.com/"

class Test2:
    @pytest.fixture()
    def setup(self):
        chrome_driver = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_driver)
        self.driver.get(URL)

    def test_login(self, setup, tear_down):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()

        assert self.driver.current_url == URL2, 'Página incorreta!'

        #assert self.driver.find_element(By.ID,'react-burger-menu-btn'), 'Menu inexistente!'

        try:
            self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            assert False, 'Menu não existente!'

        time.sleep(3)

    @pytest.fixture()
    def tear_down(self):
        yield
        self.driver.quit()
