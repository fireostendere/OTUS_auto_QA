from time import time
import allure


@allure.feature('User auth page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_user_auth_page_elements(app):
    user_auth_page = app.open_user_auth_page()
    user_auth_page.assert_element(user_auth_page._MAIN_NAV_BAR)
    user_auth_page.assert_element(user_auth_page._CONTENT_TITLE)
    user_auth_page.assert_element(user_auth_page._LOGIN_LINK_IN_FORM)
    user_auth_page.assert_element(user_auth_page._PERSONAL_DETAILS_SECTION)
    user_auth_page.assert_element(user_auth_page._AGREE_CHECKBOX)


@allure.feature('User auth page')
@allure.story('Registration')
@allure.title('Correct user registration')
def test_user_registration(app):
    user_auth_page = app.open_user_auth_page()
    uniq = int(time())
    user_auth_page.fill_first_name(f"name_{uniq}")\
                  .fill_last_name(f"surname_{uniq}")\
                  .fill_email(f"{uniq}@test.com")\
                  .fill_phone(f"+1{uniq}")\
                  .fill_password("qwerty")\
                  .fill_password_confirm("qwerty")\
                  .fill_agree_with_privacy_checkbox()\
                  .submit_continue_button()
    assert user_auth_page.driver.current_url == app.base_url + "index.php?route=account/success"
    assert user_auth_page.get_content_title_text() == "Your Account Has Been Created!"
