# Apple Music to Spotify Playlist Converter
Python application with GUI to convert Apple Music playlists to Spotify playlists.

# Install Procedure
1. Install Python 3.9+
2. From the repository root, run `pip install -r requirements.txt`
3. Modify the .env.example file to include your Apple Music and Spotify credentials, then change the extension to .env.
4. Run `python main.py`

# How to Gain API Credentials
## Apple Music
1. Pay $100 for the Apple Developer Program
## Spotify
1. Go to https://developer.spotify.com/dashboard/login
2. Log in with your Spotify account
3. Click "Create a Client ID"
4. Fill out the form with whatever information you want
5. Click "Create"
6. Copy the Client ID and Client Secret into the .env file


# Planned Features
- [ ] Add support for spotify to apple music playlist conversion
- [ ] Add support for library conversions both ways