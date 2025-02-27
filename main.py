from src.file_operations import remove_files
from src.logger import print_header
from src.ivoox import upload_to_ivoox
from src.youtube import get_latest_video_URL
from src.audio_ops import download_audio

def main():
    dataset = get_latest_video_URL()
    if dataset.len > 0:

        for data in dataset:
            file_name = download_audio(data.url, data.title)
            dataset["file_name"] = file_name
        
        upload_to_ivoox(dataset)
        remove_files('./', "*.mp3")


if __name__ == "__main__":
    print_header()
    main()
