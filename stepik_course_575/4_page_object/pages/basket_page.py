from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are in basket"

    def should_be_message_that_basket_is_empty(self):
        assert "Your basket is empty." in self.element_text(*BasketPageLocators.EMPTY_TEXT), \
            "Message that basket is empty not found"
