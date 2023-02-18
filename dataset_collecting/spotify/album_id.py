import requests
import config

access_token = config.access_token

album_title = "2001"

# Define the endpoint and parameters for searching albums
url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {access_token}"}
params = {"q": f"album:{album_title}", "type": "album"}

# Make a request to the Spotify API to search for the album
response = requests.get(url, headers=headers, params=params)
results = response.json()

# Get the first album ID from the search results
album_id = results["albums"]["items"][0]["id"]

print("album_id : ", album_id)