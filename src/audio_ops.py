import subprocess
from src.logger import log

def download_audio(url: str, title: str) -> str:
    log('Downloading audio ...')

    sanitized_title = "".join([c if c.isalnum() else "_" for c in title])
    file_name = f"{sanitized_title}.mp3"
    prompt = [
        'yt-dlp',
        '-x', '--audio-format', 'mp3',
        '-o', file_name,
        url
    ]
    subprocess.run(prompt)
    return file_name