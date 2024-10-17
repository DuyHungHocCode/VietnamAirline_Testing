import pytest
from selenium.webdriver.common.by import By
from Pages.purchaseTicket_page import PurchaseTicket_Page

@pytest.mark.usefixtures("setup")
class Test_Booking ():
    def test_CheckMaxPassengerCount(self):

        pt = PurchaseTicket_Page(self.driver)
        pt.accept_coockie()
        pt.PassengerField_click()
        pt.increaseAdultPassenger(9)

        ChildrenAged2To12 = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_child']//button[@class='psg-btn psg-increase'][normalize-space()='+']")

        if ChildrenAged2To12.get_attribute("disabled") or not ChildrenAged2To12.is_enabled():
            assert True, "Test passed:"
        else:
            pytest.fail()


    def test_CheckInfantsUnder2WithAdult(self):
        pt = PurchaseTicket_Page(self.driver)
        pt.increaseAdultPassenger(0)
        pt.increasInfantsUnder2(9)

        numberOfInfantsUnder2 = self.driver.find_element(By.ID, 'current_passenger_infant')

        assert numberOfInfantsUnder2.text == '9'