from pages.main_page import MainPage
import time

#def test_guest_can_go_to_login_page(browser):
	#link = "http://selenium1py.pythonanywhere.com/"
	#page = MainPage(browser, link)
	#page.open()
	#time.sleep(5)
	#page.go_to_login_page()

def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	time.sleep(5)
	page.should_be_login_link()
