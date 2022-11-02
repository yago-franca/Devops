from PageObjects.LoginPage import LoginPage

class Teste4:

    @pytest.fixture()
    def setup(self):
        self.login_page = LoginPage()
        yield
        self.login_page.close_page()

    def test_efetuar_login(self):
        self.login_page.efetuar_login()
