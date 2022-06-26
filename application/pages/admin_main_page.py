from selenium.webdriver.common.by import By
from application.pages.base_page import BasePage
import allure


class AdminMainPage(BasePage):
    _CATALOG_MENU_ITEM = (By.CSS_SELECTOR, "#menu-catalog")
    _PRODUCTS_MENU_ITEM = (By.XPATH, "//a[.='Products']")

    @allure.step("Open products page from admin panel menu")
    def open_admin_products_page(self):
        self.logger.info(f"{self.logger.name}: Open admin products page from menu")
        self.driver.find_element(*self._CATALOG_MENU_ITEM).click()
        self.driver.find_element(*self._PRODUCTS_MENU_ITEM).click()
