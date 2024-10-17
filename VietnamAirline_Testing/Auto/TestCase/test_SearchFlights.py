import pytest
from selenium.webdriver.common.by import By
from Pages.purchaseTicket_page import PurchaseTicket_Page
from Pages.search_flights_result_page import SearchFlightsResult

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_filghts(self):

        pt = PurchaseTicket_Page(self.driver)
        pt.accept_coockie()
        pt.setdepartureLocation("Tp. Hồ Chí Minh (SGN), Việt Nam")
        pt.setDestination("Hà Nội (HAN), Việt Nam")
        pt.openCalender()
        pt.setDepartureDate(9,15,2024)
        pt.setReturnlDate(9,20,2024)
        pt.searchFlight()

        sl = SearchFlightsResult(self.driver)
        sl.filterDepartureTimes(1)



        results = self.driver.find_elements(By.XPATH, "//div[@class='upsell-premium-row-pres-container']")
        index = 0
        total_minutes_1 = 720
        for result in results:
            departure_time_1 = result.find_elements(By.XPATH, "//div[@class='refx-display-1 bound-departure-datetime']")
            print(departure_time_1[index].text)
            hours, minutes = map(int, departure_time_1[index].text.split(":"))
            total_minutes = hours * 60 + minutes
            if total_minutes <= total_minutes_1:
                assert True
            else:
                assert False
            index += 1