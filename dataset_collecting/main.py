import lyricsgenius
import requests

import config_genius

access_token = config_genius.access_token

# Replace YOUR_ACCESS_TOKEN with your own Genius API access token
genius = lyricsgenius.Genius(access_token)

# Search for a song
song = genius.search_song('dear mama', '2pac')

album_cover_url = song.song_art_image_thumbnail_url

# Print the song's lyrics
print(song.lyrics)

response = requests.get(album_cover_url)

if response.status_code == 200:
    # Get the content of the response (the image data)
    image_data = response.content

    # Open a file and write the image data to it
    with open("cover.jpg", "wb") as f:
        f.write(image_data)
        print("Image saved successfully")
else:
    print("Failed to download image")