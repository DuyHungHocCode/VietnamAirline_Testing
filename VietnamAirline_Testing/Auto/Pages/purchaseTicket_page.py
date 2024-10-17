from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class PurchaseTicket_Page():
    def __init__(self, driver):
        self.driver = driver
    
    def accept_coockie(self):
        cookie_button = self.driver.find_element(By.XPATH, '//button[@id="cookie-agree"]')
        cookie_button.click()

    def PassengerField_click(self):
        Passenger = self.driver.find_element(By.ID, 'txtRoundTripPassenger')
        Passenger.click()

    def increaseAdultPassenger(self, PassengerCount:int):
        psg_increase = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_adult']//button[@class='psg-btn psg-increase'][normalize-space()='+']")
        for _ in range(0, PassengerCount):
            psg_increase.click()

    def decreaseAdultPassenger(self, PassengerCount:int):
        psg_decrease = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_adult']//button[@class='psg-btn psg-decrease'][normalize-space()='-']")
        for _ in range(0, PassengerCount):
            psg_decrease.click()

    def increasInfantsUnder2(self, PassengerCount:int):
        kid_under_2 = self.driver.find_element(By.XPATH, "//div[@id='selector_for_passenger_infant']//button[@class='psg-btn psg-increase'][normalize-space()='+']")
        for _ in range(0, PassengerCount):
            kid_under_2.click()

    def setdepartureLocation(self, location):
        DepartFrom = self.driver.find_element(By.XPATH, "//input[@id='city-from-roundtrip']")
        DepartFrom.clear()
        DepartFrom.send_keys(f"{location}" + Keys.ENTER)
        confirm = self.driver.find_element(By.XPATH, "//div[@class='tab-content content-form']")
        confirm.click()

    def setDestination(self, location):
        Destination = self.driver.find_element(By.XPATH, "//input[@id='city-to-roundtrip']")
        Destination.clear()
        Destination.send_keys(f"{location}" + Keys.ENTER)
        confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='box-from-wapper box-from-wapper-to']"))
        )
        confirm.click()

    def openCalender(self):
        DepartureDate_calender = self.driver.find_element(By.XPATH, "//input[@id='roundtrip-date-depart']")
        DepartureDate_calender.click()

    def setDepartureDate(self, month: int, day: int, year: int):
        DepartureDate = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//td[@data-month='{month}' and @data-year='{year}']//a[@class='ui-state-default' and contains(text(), '{day}')]"))
        )
        DepartureDate.click()

    def setReturnlDate(self, month: int, day: int, year: int):
        ReturnDate = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//td[@data-month='{month}' and @data-year='{year}']//a[@class='ui-state-default' and contains(text(), '{day}')]"))
        )
        ReturnDate.click()

    def searchFlight(self):
        confirm_date = self.driver.find_element(By.XPATH, "//div[@class='roundtrip-date move-top']//button[@class='datepicker-ctrl confirm-dates'][contains(text(),'Chọn')]")
        confirm_date.click()

        submit = self.driver.find_element(By.XPATH, "//input[@id='btnSubmitBookYourTrip']")
        submit.click()