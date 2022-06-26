from selenium.webdriver.common.by import By
from application.pages.base_page import BasePage
import allure


class AdminPage(BasePage):
    _LOGO = (By.CSS_SELECTOR, "#header-logo")
    _FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    _USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    _LOGIN_BUTTON = (By.XPATH, "//button[.=' Login']")

    @allure.step("Admin login with credentials: {login} / {password}")
    def login(self, login, password):
        self.logger.info(f"{self.logger.name}: Login with credentials: {login} / {password}")
        self.type(self._USERNAME_FIELD, login)
        self.type(self._PASSWORD_FIELD, password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()
