import pytest
from src.helpers.appiumdriver import Driver
from src.screens.news_screen import NewsScreen
from src.screens.login_screen import LoginScreen
from src.helpers.app import App


class TestLogin(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    @pytest.mark.login
    def test_login(self):
        App.is_displayed(self, NewsScreen.newsHeader)
        App.is_displayed(self, NewsScreen.accountTab)
        App.is_displayed(self, NewsScreen.hamburgerMenu)

        App.click(self, NewsScreen.hamburgerMenu)
        App.assert_text(self, NewsScreen.menuHeader, 'Menu')
        App.click(self, NewsScreen.loginButton)

        # login as real user
        LoginScreen.login_user(self)