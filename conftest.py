import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
