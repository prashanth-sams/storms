import pytest
from src.helpers.appiumdriver import Driver
from src.screens.news_screen import NewsScreen
from src.screens.login_screen import LoginScreen
from src.screens.dashboard_screen import DashboardScreen
from src.helpers.app import App


class TestLogin(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    """
    handled 3 different workflows to avoid flakiness in the login functionality
    positive case
    """
    @pytest.mark.login
    def test_login_positive(self):
        App.is_displayed(self, NewsScreen.accountTab)
        App.is_displayed(self, NewsScreen.hamburgerMenu)
        App.assert_text(self, NewsScreen.newsHeader, 'News')

        App.click(self, NewsScreen.hamburgerMenu)
        App.assert_text(self, NewsScreen.menuHeader, 'Menu')

        # login as real user
        LoginScreen.login_user(self, 'valid password')
        App.assert_text(self, NewsScreen.newsHeader, 'News')

        App.click(self, NewsScreen.accountTab)
        App.is_displayed(self, DashboardScreen.profileImage)
        App.assert_text(self, DashboardScreen.profileName, 'hack')
        App.assert_text(self, DashboardScreen.dashboardHeader, 'My Dashboard')

    """
    handled 3 different workflows to avoid flakiness in the login functionality
    negative case
    """
    @pytest.mark.login
    def test_login_negative(self):
        App.is_displayed(self, NewsScreen.accountTab)
        App.is_displayed(self, NewsScreen.hamburgerMenu)
        App.assert_text(self, NewsScreen.newsHeader, 'News')

        App.click(self, NewsScreen.hamburgerMenu)
        App.assert_text(self, NewsScreen.menuHeader, 'Menu')

        # login as real user
        LoginScreen.login_user(self, 'invalid password')
        App.assert_text(self, LoginScreen.invalidMsg, 'Incorrect username or password.')