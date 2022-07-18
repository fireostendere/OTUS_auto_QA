import pytest
import allure


@allure.feature('Main page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_main_page_elements(app):
    main_page = app.open_main_page()
    main_page.assert_element(main_page._MAIN_NAV_BAR)
    main_page.assert_element(main_page._SEARCH_FIELD)
    main_page.assert_element(main_page._MENU)
    main_page.assert_element(main_page._CART_BUTTON)
    main_page.assert_element(main_page._MAIN_SLIDER)


@allure.feature('Main page')
@allure.story('Validation')
@allure.title('Currency switcher')
@pytest.mark.parametrize("currency, currency_label", [("EUR", "€ Currency"),
                                                      ("GBP", "£ Currency"),
                                                      ("USD", "$ Currency")])
def test_switch_currency_from_main_nav(app, currency, currency_label):
    main_page = app.open_main_page()
    main_page.switch_currency_in_main_nav(to=currency)
    currency_text = main_page.get_currency_text_from_main_nav()
    assert currency_text == f"{currency_label}  "
