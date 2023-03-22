from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from sys import argv
import pyfiglet
  
result = pyfiglet.figlet_format("YtDwnlder", font = "slant"  )
print(result)

# Get link from commandline
# Eg: python ytdwnld.py "https://youtu.be/m7Bc3pLyij0"
ytlink = argv[1]

# Creating an object of youtube
ytobj = YouTube(ytlink, on_progress_callback = on_progress)

# Print some description about the youtube video
print("Title:", ytobj.title)
print("Creator:", ytobj.author)

# Download the video
ytvideo = ytobj.streams.get_highest_resolution()
ytvideo.download(r'C:\Users\MILAN\downloads')
print("\n")
print("Download Complete")


"""Documentations
pytube : https://pytube.io/en/latest/user/quickstart.html
progress bar : https://stackoverflow.com/a/68419849
"""