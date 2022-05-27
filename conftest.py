import pytest
from selenium import webdriver
from application.app import App


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://127.0.0.1:8081/")


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    return driver


@pytest.fixture
def app(request):
    browser = request.config.getoption("--browser")
    driver = driver_factory(browser)
    url = request.config.getoption("--url")
    application = App(driver=driver, base_url=url)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return application
