from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from setup import YT_CHANNEL_URL
from src.selenium_helper import click_button_by_xpath

def get_latest_video_URL():
    print('<!> Loading webdriver and URL ...')
    driver = webdriver.Chrome()
    driver.get(YT_CHANNEL_URL + '/videos')
    sleep(5)

    click_button_by_xpath(driver, '//button[span[text()="Reject all"]]', 5, True)

    try:
        print('<!> Looking for latest video ...')
        video_el = driver.find_element(By.XPATH, '//ytd-rich-grid-media[1]//a[@id="thumbnail"]')
        title_el = video_el.find_element(By.XPATH, '//ytd-rich-grid-media[1]//yt-formatted-string[@id="video-title"]')
        
        url = video_el.get_attribute('href')
        title = title_el.text
    except:
        driver.quit()
        raise Exception("<!> Latest video not found!")

    driver.quit()
    return url, title
