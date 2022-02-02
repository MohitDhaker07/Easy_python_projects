"""copy all your links in a excel sheet and then use this program """

# import the package
import csv
from pytube import YouTube

# reading csv file containing all the links of playlist

with open("yt_data.csv", "r") as file:
    reader = csv.reader(file)
    for data in reader:
        url = data

        # push the data
        for urls in url:
            my_video = YouTube(urls)

            print("*********************Video Title************************")
            # get Video Title
            print(my_video.title)

            print("********************Downloading videos*************************")
            my_video = my_video.streams.get_highest_resolution()

            # downloading the videos
            my_video.download()
