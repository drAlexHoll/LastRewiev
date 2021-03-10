from pages.product_page import ProductPage
import time
import math

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.add_book_to_bask()
    page.solve_quiz_and_get_code()
    