import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                        "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                        pytest.param("?promo=offer7",
                                                     marks=pytest.mark.xfail(reason="bug on a temporary promo page")),
                                        "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link):
    url = link + promo_link
    page = ProductPage(browser, url)
    page.open()
    page.should_be_add_to_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_same_products_in_basket_and_on_the_page()
    page.should_be_correct_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_that_basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        product_page = ProductPage(browser, login_link)
        product_page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "Qwerty1234@"

        product_page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
