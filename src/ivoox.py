from genericpath import exists
import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from setup import IVX_USERNAME, IVX_PASS, IVX_MAIN_URL, TAGS
from src.file_operations import load_cookies, save_cookies
from src.history import load_history, save_history
from src.logger import log
from src.selenium_helper import check_navigation, click_button_by_text, click_button_by_xpath, fill_input_by_placeholder, fill_input_by_xpath, get_driver_instance, click_button_when_available

def upload_to_ivoox(dataset):
    history = load_history()
    
    driver = get_driver_instance()
    driver.get(IVX_MAIN_URL)
    sleep(5)

    # cookies_file_exists = exists(COOKIES_PATH)
    # if cookies_file_exists:
    #     driver = load_cookies(driver)
    #     driver.refresh()
    # else:
    login(driver)
    #save_cookies(driver)
    is_useragent_ok = False

    # check if useragent was valid or not
    # if not, retry with new one
    log("Checking if user agent is valid...")
    while not is_useragent_ok:
        try:
            check_navigation(driver, 'dashboard')
            is_useragent_ok = True
            log('Valid user agent! Execution can continue =)')
        except:
            log('Invalid user agent. Trying new one ...')
            is_useragent_ok = False
            driver = get_driver_instance()
            driver.get(IVX_MAIN_URL)
            sleep(5)
            login(driver)




    for data in dataset :
        isUrlInHistory = data['link'] in history;
        if not isUrlInHistory:
            log('This video URL is not stored in history file. Running upload process...')
            
            try:
                # touch dashboard btn in top menu
                click_button_by_xpath(driver, '/html/body/div[2]/div/div/div[1]/header/div/div/ul/li[1]/a', shouldPass=True)

                check_navigation(driver, 'dashboard')
                click_button_by_text(driver, 'Understood', shouldPass=True)

                file_path = os.path.abspath(data['file_name'])
                click_button_by_xpath(driver, '//*[@id="content"]/div/div[2]/div/div[2]/a', 5)
            
                check_navigation(driver, 'upload')
                click_button_by_text(driver, "Continue")

                # Locate the file input field and upload the file
                log('Uploading file ...')
                _file_input_el = driver.find_element(By.XPATH, '//input[@type="file"]')
                _file_input_el.send_keys(os.path.abspath(file_path))
                sleep(2)
            
                # fill form
                fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/div/input', data['title'], 0)
                fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/textarea', data['description'], 0)

                # Insert TAGS
                tag_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[5]/div/div/div[1]/div[2]/input'
                for tag in TAGS[:5]:  # Max 5 tags
                    fill_input_by_xpath(driver, tag_input_xpath, tag, 1)
                    fill_input_by_xpath(driver, tag_input_xpath, Keys.RETURN, 1)

                sleep(2)
                click_button_when_available(driver, "Continue",5)

                print('Executing JS.for checkbox clicking..');
                driver.execute_script('''
                                    var el = document.getElementById('accept-conditions');
                                    el.click();
                                    ''')

                sleep(1)
                click_button_by_text(driver, "Publish", 10)

                history.append(data['link'])
            except:
                log('Could not upload the file!')
                continue
        else:
            log(f'Video URL stored in history! This video was uploaded previously: {data['title']}')

    driver.quit()
    save_history(history)

def login(driver):
    # close modals and other trash
    log('Closing trash modals ...')
    click_button_by_xpath(driver,'//*[@id="didomi-notice-agree-button"]', 1, True)
    click_button_by_xpath(driver, '//*[@id="__BVID__92___BV_modal_body_"]/i', 1, True)


    log("Looking for login button ...")
    click_button_by_xpath(driver,'//*[@id="__layout"]/div/div[1]/header/div/div/div[2]/div[1]/button[1]', 1)

    log('Filling pass and email ...')
    modalElement = driver.find_element(By.XPATH, f"//div[contains(concat(' ', normalize-space(@class), ' '), ' modal ')]")
    fill_input_by_placeholder(modalElement,'Email', IVX_USERNAME,0)
    fill_input_by_placeholder(modalElement,'Password', IVX_PASS,1)
    click_button_by_xpath(modalElement, "//button[@type='submit' and contains(., 'Log in')]", 5)
