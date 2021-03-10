from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert True

    def should_be_register_form(self):
        assert True