from src.file_operations import remove_files
from src.logger import print_header
from src.ivoox import upload_to_ivoox
from src.youtube import get_latest_video_URL
from src.audio_ops import download_audio

def main():
    videoList = get_latest_video_URL()

    if len(videoList) > 0:

        for video in videoList:
            file_name = download_audio(video["url"], video["title"])
            video["file_name"] = file_name
        
        upload_to_ivoox(videoList)
        # remove_files('./', "*.mp3")


if __name__ == "__main__":
    print_header()
    main()
