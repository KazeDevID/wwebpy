import time
from unittest import TestCase

from selenium import webdriver

from wwebpy.accounts.pages import LoginPage
from wwebpy.header.pages import HeaderPage


class TearDownClass:
    driver = None


class LoggedInTestCase(TearDownClass, TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # Manually login in
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.load()
        time.sleep(7)

    @classmethod
    def tearDownClass(cls):
        header_page = HeaderPage(cls.driver)
        header_page.logout()
        cls.driver.quit()


class FileBaseTestCase(TearDownClass, TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
