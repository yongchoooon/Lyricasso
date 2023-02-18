import requests
import base64
import config
import json

from image_saver import image_saver

album_id = config.album_id
access_token = config.access_token

# Define the endpoint and parameters
url = f"https://api.spotify.com/v1/albums/{album_id}"
headers = {"Authorization": f"Bearer {access_token}"}
params = {"market": "US"}

# Make a request to the Spotify API to get the album details
response = requests.get(url.format(album_id=f"{album_id}"), headers=headers, params=params)

if response.status_code == 200:
    album_data = response.json()

    resposne_data = json.dumps(album_data, indent=4)
    with open("resposne_data.json", "w") as f:
        f.write(resposne_data)
        f.close()
    
    # Get the cover image URL from the album details
    cover_url = album_data["images"][0]["url"]

    # Get the genre from album details
    if len(album_data["genres"]) == 0:
        genre = "No genre"
    else:
        genre = album_data["genres"][0]

    # Retrieve the cover image data
    response = requests.get(cover_url)
    cover_data = response.content

    # Convert the image data to base64 encoding
    cover_base64 = base64.b64encode(cover_data)

    # Print the album title 
    print("Album title: ", album_data["name"])

    # Save the image to a file
    image_saver(cover_base64.decode())
    print("Image saved successfully")

    # Print the genre
    print("Genre: ", genre)

else: 
    print("Error: ", response.status_code)

