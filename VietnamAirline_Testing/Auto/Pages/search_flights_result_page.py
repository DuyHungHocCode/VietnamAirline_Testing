from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class SearchFlightsResult:
    def __init__(self, driver):
        self.driver = driver

    def filterDepartureTimes(self, flightHour: int):
        filter_but = self.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator filters-button mat-stroked-button mat-button-base ng-star-inserted']")
        filter_but.click()

        option = self.driver.find_elements(By.XPATH, "//div[@class='radio-buttons']")
        option_1 = option[1].find_elements(By.TAG_NAME, "mat-radio-button")

        if flightHour == 1:
            zeroToTwelveAM = option_1[1]
            zeroToTwelveAM.click()
        elif flightHour == 2:
            twelveToSixPM = option_1[2]
            twelveToSixPM.click()
        elif flightHour == 3:
            sixtoTwelvePM = option_1[3]
            sixtoTwelvePM.click()
      
        apply_but = self.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator apply mat-flat-button mat-button-base']")
        apply_but.click()


