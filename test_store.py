from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_button_existance(browser):
    
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    
    browser.get(link)
    
    add_button = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.btn-add-to-basket')
    ))
    
    assert add_button