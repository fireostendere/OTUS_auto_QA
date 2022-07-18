from application.pages.admin_auth_page import AdminPage
from application.pages.catalog_page import CatalogPage
from application.pages.main_page import MainPage
from application.pages.product_page import ProductPage
from application.pages.user_auth_page import UserAuthPage
from selenium.common.exceptions import NoAlertPresentException
import logging
import allure


class App:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.__config_logger()
        self.main_page = None
        self.catalog_page = None
        self.product_page = None
        self.admin_page = None
        self.user_auth_page = None

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(self.driver.log_path))
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Open main page")
    def open_main_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}")
        self.driver.get(self.base_url)
        if not self.main_page:
            self.main_page = MainPage(self)
        return self.main_page

    @allure.step("Open catalog page")
    def open_catalog_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/smartphone")
        self.driver.get(self.base_url + "/smartphone")
        if not self.catalog_page:
            self.catalog_page = CatalogPage(self)
        return self.catalog_page

    @allure.step("Open product page")
    def open_product_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/mp3-players/ipod-classic")
        self.driver.get(self.base_url + "/mp3-players/ipod-classic")
        if not self.product_page:
            self.product_page = ProductPage(self)
        return self.product_page

    @allure.step("Open admin page")
    def open_admin_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/admin/")
        self.driver.get(self.base_url + "/admin/")
        if not self.admin_page:
            self.admin_page = AdminPage(self)
        return self.admin_page

    @allure.step("Open user_auth page")
    def open_user_auth_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/index.php?route=account/register")
        self.driver.get(self.base_url + "/index.php?route=account/register")
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            pass
        else:
            alert_obj = self.driver.switch_to.alert
            alert_obj.accept()

        if not self.user_auth_page:
            self.user_auth_page = UserAuthPage(self)
        return self.user_auth_page
