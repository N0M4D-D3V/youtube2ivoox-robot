import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from setup import DESCRIPTION, IVX_USERNAME, IVX_PASS, IVX_MAIN_URL, TAGS
from src.selenium_helper import check_navigation, click_button_by_text, click_button_by_xpath, fill_input_by_xpath

def upload_to_ivoox(file_path: str, title: str):
    file_path = os.path.abspath(file_path)

    driver = webdriver.Chrome()
    driver.get(IVX_MAIN_URL)
    sleep(5)

    # close modals and other trash
    print('<!> Closing trash modals ...')
    click_button_by_xpath(driver,'//*[@id="didomi-notice-disagree-button"]', 1, True)
    click_button_by_xpath(driver, '//*[@id="__BVID__92___BV_modal_body_"]/i', 1, True)


    print("<!> Looking for login button ...")
    click_button_by_xpath(driver,'//*[@id="__layout"]/div/div[1]/header/div/div/div[2]/div[1]/button[1]', 1)

    print('<!> Filling pass and email ...')
    fill_input_by_xpath(driver,'//*[@id="email-field"]', IVX_USERNAME,0)
    fill_input_by_xpath(driver,'/html/body/div[5]/div[1]/div/div/div/div/div/span/form/div[2]/div/div/div/input', IVX_PASS,0)
    sleep(1)


    click_button_by_xpath(driver, '/html/body/div[5]/div[1]/div/div/div/div/div/span/form/div[4]/button', 5)
    
    check_navigation(driver, 'dashboard')
    click_button_by_text(driver, 'Understood')

    click_button_by_xpath(driver, '//*[@id="content"]/div/div[2]/div/div[2]/a', 5)
    
    check_navigation(driver, 'upload')
    click_button_by_text(driver, "Continue")

    # Locate the file input field and upload the file
    try:
        print('<!> Uploading file ...')
        _file_input_el = driver.find_element(By.XPATH, '//input[@type="file"]')
        _file_input_el.send_keys(os.path.abspath(file_path))
        sleep(20)
    except:
        driver.quit()
        raise Exception('<!> Could not upload the file!')
    
    # fill form
    fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/div/input', title, 0)
    fill_input_by_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/textarea', DESCRIPTION, 0)

    # Insert TAGS
    tag_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[5]/div/div/div[1]/div[2]/input'
    for tag in TAGS[:5]:  # Max 5 tags
        fill_input_by_xpath(driver, tag_input_xpath, tag, 1)
        fill_input_by_xpath(driver, tag_input_xpath, Keys.RETURN, 1)

    sleep(2)
    click_button_by_text(driver, "Continue",5)
    click_button_by_xpath(driver, '//*[@id="accept-conditions"]', 1)
    click_button_by_text(driver, "Publish",5)


    driver.quit()

