from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from sys import argv

import pyfiglet
  
result = pyfiglet.figlet_format("YtDwnlder")
print("\n")
print(result)
print("Created by Milan Sony \nhttps://linktr.ee/milansony\n")

def dwnldavideo():
  # Get link from commandline
  # Eg: python ytdwnld.py "https://youtu.be/m7Bc3pLyij0"
  ytlink = input("Youtube video link: ")

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
  print("\n")

def dwnldaplaylist():
  print("playlist")

def dwnldachannel():
  print("channel")

def main():
  while True:
    print("Enter your choice")
    print("1. Download a youtube video \n2. Download a youtube playlist \n3. Download all of the videos created by a channel \n4. Exit")
    choice = input("Please enter your choice: ")

    if (choice == '1'):
      dwnldavideo()
    elif (choice == '2'):
      dwnldaplaylist()
    elif (choice == '3'):
      dwnldachannel()
    elif (choice == '4'):
      print("You have choose exit | Type: python ytdwnld.py to run again")
      print("\n")
      exit()
    else:
      print("Invalid choice. Please try again\n")

main()