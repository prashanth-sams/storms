import pytest
from src.helpers.appiumdriver import Driver
from src.screens.android.home_screen import HomeScreen
from src.helpers.app import App


class TestHome(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)

    @pytest.mark.home
    def test_home_1(self):
        App.element(self, HomeScreen.homeMenu)
        App.element(self, HomeScreen.loginMenu)
        App.element(self, HomeScreen.formsMenu)
        App.element(self, HomeScreen.swipeMenu)

    @pytest.mark.home
    def test_home_2(self):
        App.element(self, HomeScreen.homeMenu)
        App.element(self, HomeScreen.loginMenu)