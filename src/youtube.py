from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from setup import YT_CHANNEL_URLS
from src.selenium_helper import click_button_by_xpath

def get_latest_video_URL():
    print('[Y2I Robot] Loading webdriver and URL ...')
    dataset = []
    driver = webdriver.Chrome()

    for channel in YT_CHANNEL_URLS:

        driver.get(channel)
        sleep(5)

        click_button_by_xpath(driver, '//button[span[text()="Reject all"]]', 5, True)

        try:
            print('[Y2I Robot] Looking for latest video ...')
            video_el = driver.find_element(By.XPATH, '//ytd-rich-grid-media[1]//a[@id="thumbnail"]')
            title_el = video_el.find_element(By.XPATH, '//ytd-rich-grid-media[1]//yt-formatted-string[@id="video-title"]')
            
            url = video_el.get_attribute('href')
            title = title_el.text

            print(f'[Y2I Robot] Video: {title}')
            dataset.append({'title': title, 'url': url})
        except:
            raise Exception(f'[Y2I Robot] Latest video not found for "{url}"!')

    driver.quit()
    return dataset
