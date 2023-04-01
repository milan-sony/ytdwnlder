from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 

import pyfiglet

result = pyfiglet.figlet_format("YtDwnlder")
print("\n")
print(result)
print("Created by Milan Sony \nhttps://linktr.ee/milansony")

def dwnldavideo():
  print("\n")
  print("You have choose 1 | Download a youtube video")
  ytlink = input("Youtube video link: ")

  # Creating an object of youtube
  ytobj = YouTube(ytlink, on_progress_callback = on_progress)

  # Print some description about the youtube video
  print("Title:", ytobj.title)
  print("Creator:", ytobj.author)
  print("\n")

  print("Dowloading in progress")

  # Download the video
  ytvideo = ytobj.streams.get_highest_resolution()

  ytvideo.download(r'C:\Users\MILAN\downloads')
  print("\n")
  print("Download Complete")
  print (f'RES: {ytvideo.resolution}\nFPS: {ytvideo.fps}\nTYPE: {ytvideo.subtype}')

def dwnldaudio():
  print("\n")
  print("You have choose 2 | Download audio from a youtube video")
  ytlink = input("Youtube video link: ")

  ytobj = YouTube(ytlink)

  # Print some description about the youtube video
  print("Title:", ytobj.title)
  print("Creator:", ytobj.author)
  print("\n")

  print("Dowloading in progress")

  yt_stream = ytobj.streams.filter(only_audio=True, mime_type='audio/mp4')

  if yt_stream:
    yt_stream = yt_stream[1]

  print (f'BITRATE: {yt_stream.abr}\nTYPE: {yt_stream.subtype}')
  yt_stream.download(r'C:\Users\MILAN\downloads')
  print("\n")
  print("Download Complete")

def main():
  while True:
    print("\n")
    print("Enter your choice")
    print("1. Download a youtube video \n2. Download audio from a youtube video \n3. Exit")
    choice = input("Please enter your choice: ")

    if (choice == '1'):
      dwnldavideo()
    elif (choice == '2'):
      dwnldaudio()
    elif (choice == '3'):
      print("You have choose exit | Type: python ytdwnld.py to run again")
      print("\n")
      exit()
    else:
      print("Invalid choice. Please try again\n")

main()