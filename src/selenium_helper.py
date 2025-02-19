from time import sleep
from selenium.webdriver.common.by import By

def click_button_by_text(driver, button_text, sleep_time=2, shouldPass = False):
    try:
        print(f'<!> Looking for "{button_text}" BTN ...')
        el = driver.find_element(By.XPATH, f'//button[contains(text(), "{button_text}")]')
        el.click()
        sleep(sleep_time)
    except:
        if shouldPass:
            print('<!> Button not found. Script can continue ...')
            pass
        else:
            driver.quit()
            raise Exception('<!> BTN not found!')
    
def click_button_by_xpath(driver, xpath, sleep_time=2, shouldPass=False):
    try:
        print(f'<!> Looking for "{xpath}" button ...')
        el = driver.find_element(By.XPATH, xpath)
        el.click();
        sleep(sleep_time)
    except:
        if shouldPass:
            print('<!> Button not found. Script can continue ...')
            pass
        else:
            driver.quit()
            raise Exception("<!> Button not found!")


def check_navigation(driver, keyword):
    curr_url: str = driver.current_url
    if keyword in curr_url:
        pass
    else:
        driver.quit()
        raise Exception('<!> Error: "'+keyword + '" not found in current URL.')
    
def fill_input_by_xpath(driver, xpath, value, sleep_time=1):
    try:
        el = driver.find_element(By.XPATH, xpath)
        el.send_keys(value)
        sleep(sleep_time)
    except:
        driver.quit()
        raise Exception('<!> Could not fill input')