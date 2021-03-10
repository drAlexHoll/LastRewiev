from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

