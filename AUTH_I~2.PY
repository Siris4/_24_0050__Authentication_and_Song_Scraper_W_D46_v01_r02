
import os
import base64
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# setup env vars based on EnvVarMaster values:
CLIENT_ID = os.environ.get('CLIENT_ID', 'Client ID does not exist')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', 'Client Secret does not exist')
BASE_URL = os.environ.get('BASE_URL', 'Base URL does not exist')
REDIRECT_URI = os.environ.get('REDIRECT_URI', 'Redirect URI does not exist')
CACHE_PATH = os.environ.get('CACHE_PATH', 'Cache path does not exist')

print(f"The CLIENT_ID is: {CLIENT_ID}")
print(f"The CLIENT_SECRET is: {CLIENT_SECRET}")
print(f"The BASE_URL is: {BASE_URL}")
print(f"The REDIRECT_URI is: {REDIRECT_URI}")
print(f"The CACHE_PATH is: {CACHE_PATH}")

def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = requests.post(BASE_URL, headers=headers, data=data)
    json_result = result.json()
    token = json_result.get("access_token")
    return token

# For Spotify Web API access
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=REDIRECT_URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path=CACHE_PATH  # Specify a path to store the token
))

# Your web scraping and song processing logic here
