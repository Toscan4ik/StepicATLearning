import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')
    
@pytest.fixture(scope='function')
def browser(request):
    
    user_lang = request.config.getoption('language')
    
    
    print(f'\nstart chrome for test...')
    opts = Options()
    opts.add_experimental_option('prefs', 
                                {'intl.accept_languages': user_lang})
        
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=opts
    )
    
    yield browser
    
    browser.quit()