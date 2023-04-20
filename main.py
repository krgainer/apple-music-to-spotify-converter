import requests
import json
from dotenv import load_dotenv
import os

load_dotenv() # load environment variables from .env file
musickit_access_token = os.getenv("MUSICKIT_ACCESS_TOKEN")
music_user_token = os.getenv("MUSIC_USER_TOKEN")
# set up the API endpoint URL
endpoint = "https://api.music.apple.com/v1/me/library/playlists"

# set up the headers with the MusicKit developer credentials
headers = {
    "Authorization": f"Bearer {music_user_token}",
    "Music-User-Token": f"{musickit_access_token}",
    "Content-Type": "application/json",
}

# send the request to the API endpoint
response = requests.get(endpoint, headers=headers)

# parse the JSON response
playlists = json.loads(response.text)

# print the playlist data
for playlist in playlists["data"]:
    print(playlist["attributes"]["name"])