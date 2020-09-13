from appium import webdriver
import unittest
import os
from datetime import datetime
import pytest


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global desired_caps

        self.logger.info("Configuring desired capabilities")

        if self.app == 'android': desired_caps = self.android()

        self.logger.info("Initiating Appium driver")
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

        # set waits
        self.driver.implicitly_wait(5)  # waits 5 seconds

    def android(self):
        if self.device == 'emulator':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Storms_0_2_5_778_Prod.apk', noReset=True)
        elif self.device == 'real device':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Storms_0_2_5_778_Prod.apk', noReset=True)

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device, get_logger):
        self.app = app
        self.device = device
        self.logger = get_logger


if __name__ == '__main__':
    unittest.main()
