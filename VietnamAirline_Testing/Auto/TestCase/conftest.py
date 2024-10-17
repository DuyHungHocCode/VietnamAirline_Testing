
import pytest
from selenium import webdriver
import undetected_chromedriver as uc

@pytest.fixture(scope= "class")
def setup(request):
    driver = uc.Chrome(headless=False,use_subprocess=False)
    driver.get("https://www.vietnamairlines.com/vn/vi/buy-tickets-other-products/booking-and-manage-bookings/book-tickets")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    # yield driver
    # driver.quit()