"""
In order to run this code without error you need to install the next library:
- pip install azapi.
"""
import azapi

API = azapi.AZlyrics('duckduckgo', accuracy=0.5)

API.artist = 'Taylor Swift'
API.title = 'Bad Blods'

API.getLyrics(save=False, ext='lrc')

print(API.lyrics)

# Correct Artist and Title are updated from webpage
print(API.title, API.artist)