from setup import YT_CHANNEL_ID
from src.file_operations import remove_files
from src.logger import print_header, log
from src.ivoox import upload_to_ivoox
from src.youtube import get_last_15_videos, get_latest_video_URL
from src.audio_ops import download_audio

def main():
    videoList = []
    if not YT_CHANNEL_ID:
        log('Channel ID not provided. Using selenium...')
        videoList = get_latest_video_URL()

    else:
        log('Channel ID provided. Using XML request...')
        videoList = get_last_15_videos()

    if len(videoList) > 0:

        for video in videoList:
            file_name = download_audio(video["link"], video["title"])
            video["file_name"] = file_name
        
        upload_to_ivoox(videoList)
        remove_files('./', "*.mp3")


if __name__ == "__main__":
    print_header()
    main()
