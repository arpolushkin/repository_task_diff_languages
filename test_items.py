from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_addtobasket(browser): #checking if Add To Busket button is on the page
    
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), \
        "Кнопка добавления в корзину отсутствует"
    time.sleep(10) #to able to see the language, достаточно времени увидеть что страница на испанском