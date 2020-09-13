from appium.webdriver.common.mobileby import MobileBy
from src.helpers.appiumdriver import Driver


class HomeScreen(Driver):
    """
    home screen locators
    """
    loginMenu = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Login']/android.widget.TextView")
    formsMenu = (MobileBy.ACCESSIBILITY_ID, "Forms")

    def __init__(self, driver):
        super().__init__(driver)