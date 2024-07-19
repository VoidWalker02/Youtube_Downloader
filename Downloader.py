from pytube import YouTube
from pydub import AudioSegment  
import os
import yt_dlp


def download_video(url, output_path, format):
    try:
        ydl_opts = { #ydl_opts sets up the configuration for the download
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'format': 'best',  # Change format to something more general
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', #this apparently mimics a real user so I don't get blocked.
            }
        }
        if format == 'audio':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio', #extract audio from downloaded file
                'preferredcodec': 'mp3', #choose mp3 as file format
                'preferredquality': '192',
            }]
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True) #extract some information about the video to display at the end
            print(f"Downloaded: {info_dict.get('title', 'video')}")
    except Exception as e:
        print(f"Error: {e}")


video_url = input("Enter the video URL: ")
format_choice = input("Do you wish to download in audio or video? ").lower()
if format_choice not in ['audio', 'video']:
    print("Please enter a valid format.")
else:
    download_path = "/home/isaacm/Downloads/"
    download_video(video_url, download_path, format_choice)


