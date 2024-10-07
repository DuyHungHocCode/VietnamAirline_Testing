import os
import pytest
from selenium import webdriver

@pytest.fixture(scope= "class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    os.environ['PATH'] += "D:/selenium"
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.vietnamairlines.com/vn/vi/buy-tickets-other-products/booking-and-manage-bookings/book-tickets")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()