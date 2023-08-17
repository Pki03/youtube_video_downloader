# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:54:18 2023
@author: 91913
"""

from pytube import YouTube

url = "https://youtu.be/FQTQD3WHlCk?t=1"

sample_video = YouTube(url)

print("Video title:", sample_video.title)
print("Thumbnail URL:", sample_video.thumbnail_url)

video_stream = sample_video.streams.get_highest_resolution()

# Change the download path to your desired location
download_path = "C:/Users/91913/Downloads/videos_downloaded"  # Modify this path

video_stream.download(output_path=download_path)

print("Video downloaded successfully.")
