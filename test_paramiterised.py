import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_HubSpot(BaseTest):

    @pytest.mark.parametrize(
                            "usrnam, passwrd",
                            [
                                ("admin@gmail.com", "admin123"),
                                ("naveen@gmail.com", "naveen123")
                            ]
                            )
    def test_login(self, usrnam, passwrd):
        """
        This is for login in the hubspot application
        :param usrnam:
        :param passwrd:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login/legacy")
        self.driver.find_element(By.ID, "username").send_keys(usrnam)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys(passwrd)
        time.sleep(3)


