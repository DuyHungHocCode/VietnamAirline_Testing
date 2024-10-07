import os
import pytest
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("setup")
class Test_Booking ():
    def test_checkMaxpsg(self):

        # wait = WebDriverWait(self.driver, 10)
        cookie_button = self.driver.find_element(By.XPATH, '//button[@id="cookie-agree"]')
        cookie_button.click()


        Passenger = self.driver.find_element(By.ID, 'txtRoundTripPassenger')
        Passenger.click()

        psg_increase = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_adult']//button[@class='psg-btn psg-increase'][normalize-space()='+']")
        for _ in range(0, 9):
            psg_increase.click()

        kid_2_12 = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_child']//button[@class='psg-btn psg-increase'][normalize-space()='+']")

        if kid_2_12.get_attribute("disabled") or not kid_2_12.is_enabled():
            assert True, "Test passed:"
        else:
            pytest.fail()


# a = BookingTest()
# a.test_checkMaxpsg()