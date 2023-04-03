import socks
import socket
from pytube import YouTube
# import telegram

# you_tube_getter_bot
# Use this token to access the HTTP API:
# 5944060449:AAGtnddzZ6IWX1-IjSgUWfXDMauujVWHNr4

# Replace YOUR_BOT_TOKEN with your bot token
# bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Replace YOUR_CHAT_ID with your chat ID
# chat_id = 'YOUR_CHAT_ID'

# Replace YOUR_PROXY_HOST and YOUR_PROXY_PORT with your proxy host and port
proxy_host = '127.0.0.1'
proxy_port = '10808'

# Set the SOCKS proxy for pytube
socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
socket.socket = socks.socksocket

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{percentage_of_completion:.2f}% downloaded")


# Replace YOUR_YOUTUBE_VIDEO_URL with your YouTube video URL
url = 'https://www.youtube.com/watch?v=JJwYUMq0IFE'
yt = YouTube(url, on_progress_callback=progress_callback)
# print(yt.title)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
# print(video.resolution)
# video = yt.streams.filter(file_extension='mp4').get_by_resolution('360p').download()

# Send the video to the user
# bot.send_video(chat_id=chat_id, video=open(video, 'rb'))