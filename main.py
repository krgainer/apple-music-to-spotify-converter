import requests
import json
# from dotenv import load_dotenv
import os

# load_dotenv() # load environment variables from .env file
# musickit_access_token = os.getenv("MUSICKIT_ACCESS_TOKEN")
# music_user_token = os.getenv("MUSIC_USER_TOKEN")

import requests
from bs4 import BeautifulSoup

# set up the URL of the public playlist
url = "https://music.apple.com/us/playlist/10-10/pl.u-NpXmYm7uRmWrEW"

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# extract the playlist name and track list
playlist_name = soup.select_one("h1.product-header__title").text
track_list = [track.text.strip() for track in soup.select("div.song-name.typography-caption")]

# print the playlist name and track list
print("Playlist Name:", playlist_name)
print("Track List:")
for i, track in enumerate(track_list, start=1):
    print(f"{i}. {track}")







# set up the API endpoint URL
# endpoint = "https://api.music.apple.com/v1/me/library/playlists"

# # set up the headers with the MusicKit developer credentials
# headers = {
#     "Authorization": f"Bearer {music_user_token}",
#     "Music-User-Token": f"{musickit_access_token}",
#     "Content-Type": "application/json",
# }

# # send the request to the API endpoint
# response = requests.get(endpoint, headers=headers)

# # parse the JSON response
# playlists = json.loads(response.text)

# # print the playlist data
# for playlist in playlists["data"]:
#     print(playlist["attributes"]["name"])