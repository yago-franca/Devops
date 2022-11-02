
import time
import pytest

from PageObjects.LoginPage import LoginPage


class Test3:
    @pytest.fixture()
    def setup(self):
        self.login_page = LoginPage()
        yield
        self.login_page.close_page()

    def test_click_login_btn(self, setup):
        self.login_page.click_login_btn()
        assert self.login_page.has_login_message_error()

        time.sleep(3)