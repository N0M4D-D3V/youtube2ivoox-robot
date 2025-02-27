import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from setup import DESCRIPTION, IVX_USERNAME, IVX_PASS, IVX_MAIN_URL, TAGS
from src.history import load_history, save_history
from src.selenium_helper import check_navigation, click_button_by_text, click_button_by_xpath, fill_input_by_placeholder, fill_input_by_xpath

def upload_to_ivoox(dataset):
    history = load_history()
    
    driver = webdriver.Chrome()
    driver.get(IVX_MAIN_URL)
    sleep(5)

    login(driver)
    
    check_navigation(driver, 'dashboard')
    click_button_by_text(driver, 'Understood')

    for data in dataset:
        isUrlInHistory = data.url in history;
        if not isUrlInHistory:
            print('[Y2I Robot] This video URL is stored in history file. Aborting script execution ...')
            file_path = os.path.abspath(data.file_path)
            click_button_by_xpath(driver, '//*[@id="content"]/div/div[2]/div/div[2]/a', 5)
        
            check_navigation(driver, 'upload')
            click_button_by_text(driver, "Continue")

            # Locate the file input field and upload the file
            try:
                print('[Y2I Robot] Uploading file ...')
                _file_input_el = driver.find_element(By.XPATH, '//input[@type="file"]')
                _file_input_el.send_keys(os.path.abspath(file_path))
                sleep(100)
            except:
                print('[Y2I Robot] Could not upload the file!')
                continue
        
            # fill form
            fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/div/input', data.title, 0)
            fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/textarea', DESCRIPTION, 0)

            # Insert TAGS
            tag_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[5]/div/div/div[1]/div[2]/input'
            for tag in TAGS[:5]:  # Max 5 tags
                fill_input_by_xpath(driver, tag_input_xpath, tag, 1)
                fill_input_by_xpath(driver, tag_input_xpath, Keys.RETURN, 1)

            sleep(2)
            click_button_by_text(driver, "Continue",5)

            print('[Y2I Robot] Executing JS.for checkbox clicking..');
            driver.execute_script('''
                                var el = document.getElementById('accept-conditions');
                                el.click();
                                ''')

            sleep(1)
            click_button_by_text(driver, "Publish", 10)

            history.append(data.url)
        else:
            print('[Y2I Robot] Video URL not stored in history file. Script can continue!')

    driver.quit()
    save_history(history)

def login(driver):
    # close modals and other trash
    print('[Y2I Robot] Closing trash modals ...')
    click_button_by_xpath(driver,'//*[@id="didomi-notice-agree-button"]', 1, True)
    click_button_by_xpath(driver, '//*[@id="__BVID__92___BV_modal_body_"]/i', 1, True)


    print("[Y2I Robot] Looking for login button ...")
    click_button_by_xpath(driver,'//*[@id="__layout"]/div/div[1]/header/div/div/div[2]/div[1]/button[1]', 1)

    print('[Y2I Robot] Filling pass and email ...')
    modalElement = driver.find_element(By.XPATH, f"//div[contains(concat(' ', normalize-space(@class), ' '), ' modal ')]")
    fill_input_by_placeholder(modalElement,'Email', IVX_USERNAME,0)
    fill_input_by_placeholder(modalElement,'Password', IVX_PASS,1)
    click_button_by_xpath(modalElement, "//button[@type='submit' and contains(., 'Log in')]", 5)