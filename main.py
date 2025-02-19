from src.logger import print_header
from src.ivoox import upload_to_ivoox
from src.history import load_history, save_history
from src.youtube import get_latest_video_URL
from src.audio_ops import download_audio

def main():

    history = load_history()
    url, title = get_latest_video_URL()

    print('\n<!> Latest video URL: ' + url)
    print('<!> Latest video title: ' + title + '\n')

    print('<!> Checking history ...')
    isUrlInHistory = url in history;

    if isUrlInHistory:
        print('<!> This video URL is stored in history file. Aborting script execution ...')
    else:
        print('<!> Video URL not stored in history file. Script can continue!')
        file_name = download_audio(url, title)
        
        upload_to_ivoox(file_name, title)
        history.append(url)
        save_history(history)

if __name__ == "__main__":
    print_header()
    main()
