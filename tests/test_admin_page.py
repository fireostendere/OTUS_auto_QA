from time import time
from time import sleep
from application.pages.admin_main_page import AdminMainPage
from application.pages.admin_products_page import AdminProductsPage
import allure


@allure.feature('Admin auth page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_admin_page_elements(app):
    admin_page = app.open_admin_page()
    admin_page.assert_element(admin_page._LOGO)
    admin_page.assert_element(admin_page._FORM_TITLE)
    admin_page.assert_element(admin_page._USERNAME_FIELD)
    admin_page.assert_element(admin_page._PASSWORD_FIELD)
    admin_page.assert_element(admin_page._LOGIN_BUTTON)


@allure.feature('Admin panel')
@allure.story('Products')
@allure.title('Add product')
def test_add_new_product_from_admin(app):
    admin_user = {"login": "user", "password": "bitnami"}
    uniq = int(time())
    product = {"name": f"PRODUCT_{uniq}", "tag": f"TAG_{uniq}", "model": f"MODEL_{uniq}"}
    admin_auth_page = app.open_admin_page()
    admin_auth_page.login(admin_user["login"], admin_user["password"])
    AdminMainPage(app).open_admin_products_page()
    admin_products_page = AdminProductsPage(app)
    admin_products_page.init_product_add()\
                       .fill_product_name(product["name"])\
                       .fill_product_meta_tag(product["tag"])\
                       .open_data_tab()\
                       .fill_product_model(product["model"])\
                       .save_product()
    assert admin_products_page.is_product_in_list(product["name"])


@allure.feature('Admin panel')
@allure.story('Products')
@allure.title('Remove product')
def test_remove_product_from_admin(app):
    admin_user = {"login": "user", "password": "bitnami"}
    admin_auth_page = app.open_admin_page()
    admin_auth_page.login(admin_user["login"], admin_user["password"])
    AdminMainPage(app).open_admin_products_page()
    admin_products_page = AdminProductsPage(app)
    products_before = admin_products_page.get_products_rows()
    admin_products_page.mark_product_checked(products_before[-1])\
                       .click_product_delete_button()\
                       .confirm_product_delete()
    products_after = admin_products_page.get_products_rows()
    assert len(products_after) == len(products_before) - 1
