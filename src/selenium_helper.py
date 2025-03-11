from time import sleep
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from setup import USER_AGENTS
from src.logger import log
from src.utils import random_number

def get_driver_instance():
    user_agent = random.choice(USER_AGENTS)

    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    return webdriver.Chrome(options=options)


def click_button_by_text(driver, button_text, sleep_time=2, shouldPass = False):
    random_sleeptime = random_number(sleep_time, sleep_time+3)

    try:
        log(f'Looking for "{button_text}" BTN ...')
        el = driver.find_element(By.XPATH, f'//button[contains(., "{button_text}")]')
        el.click()
        sleep(random_sleeptime)
    except:
        if shouldPass:
            log('Button not found. Script can continue ...')
            pass
        else:
            driver.quit()
            raise Exception('[Y2I Robot] BTN not found!')
    
def click_button_by_xpath(driver, xpath, sleep_time=2, shouldPass=False):
    random_sleeptime = random_number(sleep_time, sleep_time+3)

    try:
        log(f'Looking for "{xpath}" button ...')
        el = driver.find_element(By.XPATH, xpath)
        el.click();
        sleep(random_sleeptime)
    except:
        if shouldPass:
            log('Button not found. Script can continue ...')
            pass
        else:
            driver.quit()
            raise Exception("[Y2I Robot] Button not found!")


def check_navigation(driver, keyword):
    curr_url: str = driver.current_url
    if keyword in curr_url:
        pass
    else:
        driver.quit()
        raise Exception('[Y2I Robot] Error: "'+keyword + '" not found in current URL.')
    
def fill_input_by_xpath(driver, xpath, value, sleep_time=1):
    random_sleeptime = random_number(sleep_time, sleep_time+3)

    try:
        el = driver.find_element(By.XPATH, xpath)
        el.send_keys(value)
        sleep(random_sleeptime)
    except:
        driver.quit()
        raise Exception('[Y2I Robot] Could not fill input')
    
def fill_input_by_placeholder(driver, placeholder, value, sleep_time=1):
    random_sleeptime = random_number(sleep_time, sleep_time+3)
    
    try:
        el = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
        el.send_keys(value)
        sleep(random_sleeptime)
    except:
        driver.quit()
        raise Exception('[Y2I Robot] Could not fill input')