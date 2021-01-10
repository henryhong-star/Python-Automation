import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="chrome", help="my option: chrome,firefox,edge"
    )


@pytest.fixture(scope='class')
def invoke_browser(request):

    browser_option = request.config.getoption("browser_type")

    if browser_option == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_option == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_option == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    driver.get("http://automationpractice.com/index.php")

    driver.maximize_window()

    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield

    driver.close()
