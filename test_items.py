from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_addtobasket(browser): #checking if Add To Busket button is on the page
    
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(5) #to able to see the language, достаточно времени увидеть что страница на испанском