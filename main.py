import socks
import socket
from pytube import YouTube

proxy_host = '127.0.0.1'
proxy_port = '10808'

# Set the SOCKS proxy for pytube
socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
socket.socket = socks.socksocket

def progress_callback(stream, chunk, bytes_remaining) -> None:
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{percentage_of_completion:.2f}% downloaded")

def download_video(url: str) -> None:
    yt = YouTube(url, on_progress_callback=progress_callback)
    # print(yt.title)

    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    # print(video.resolution)
    # video = yt.streams.filter(file_extension='mp4').get_by_resolution('360p').download()

with open('urls.txt') as f:
    for line in f:
        download_video(line.rstrip())

