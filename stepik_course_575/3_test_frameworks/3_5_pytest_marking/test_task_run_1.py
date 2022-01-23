import pytest


class TestMainPage:
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket:
    @pytest.mark.skip(reason="not implemented yed")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment(self, browser):
        assert True

    @pytest.mark.smoke
    def test_gest_can_see_total_price(self, browser):
        assert True


