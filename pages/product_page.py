from selenium.common.exceptions import NoAlertPresentException
from .main_page import MainPage
import math

class ProductPage(MainPage):
    def add_book_to_bask(self):
        but_find = self.browser.find_element_by_css_selector("[data-loading-text='Adding...']").click()
    
    def should_be_book_added(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_BOOK), "the message book is not present"

        self.book_titel = self.browser.find_element(*ProductPageLocators.BOOK_TITEL).text
        self.book_titel_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITEL).text[:27]

        print(self.book_titel_message)
        print(self.book_titel)
        
        assert book_titel == book_titel_message

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
