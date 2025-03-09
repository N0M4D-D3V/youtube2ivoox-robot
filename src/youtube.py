from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import urllib.request
from xml.etree import ElementTree

from setup import DESCRIPTION, YT_CHANNEL_ID, YT_CHANNEL_URLS
from src.selenium_helper import click_button_by_xpath
from src.logger import log

# Namespaces dictionary
NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'media': 'http://search.yahoo.com/mrss/'
}

def get_latest_video_URL():
    log('Loading webdriver and URL...')
    dataset = []
    driver = webdriver.Chrome()

    for channel in YT_CHANNEL_URLS:

        driver.get(channel)
        sleep(5)

        click_button_by_xpath(driver, '//button[span[text()="Reject all"]]', 5, True)

        try:
            log('Looking for latest video...')
            video_el = driver.find_element(By.XPATH, '//ytd-rich-grid-media[1]//a[@id="thumbnail"]')
            title_el = video_el.find_element(By.XPATH, '//ytd-rich-grid-media[1]//yt-formatted-string[@id="video-title"]')
            
            url = video_el.get_attribute('href')
            title = title_el.text

            log(f'Video: {title}')
            dataset.append({'title': title, 'link': url, 'description': DESCRIPTION})
        except:
            raise Exception(f'[Y2I Robot] Latest video not found for "{url}"!')

    driver.quit()
    return dataset

def get_last_15_videos():
    log('Getting last 15 videos...')
    
    # Get RSS
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={YT_CHANNEL_ID}"
    response = urllib.request.urlopen(url)
    xml_data = response.read()

    # XML Parser
    root = ElementTree.fromstring(xml_data)

    videos = []
    for entry in root.findall('atom:entry', NS):
        video_data = {
            'video_id': entry.find('yt:videoId', NS).text,
            'title': entry.find('atom:title', NS).text,
            'description': entry.find('media:group/media:description', NS).text if entry.find('media:group/media:description', NS) is not None else '',
            'link': entry.find("atom:link[@rel='alternate']", NS).attrib['href'],
            'published': entry.find('atom:published', NS).text,
            'updated': entry.find('atom:updated', NS).text
        }
        videos.append(video_data)

    for idx, video in enumerate(videos, 1):
        print(f"Video {idx}:")
        print(f"ID: {video['video_id']}")
        print(f"Title: {video['title']}")
        print(f"Published: {video['published']}")
        print(f"Updated: {video['updated']}")
        print(f"Link: {video['link']}")

        if video['description']:
            print(f"Description: {video['description'][:25]}...")
        print(f'>----------------------------------------\n')

    return videos
