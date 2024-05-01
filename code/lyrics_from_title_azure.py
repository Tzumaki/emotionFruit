"""
In order to run this code without error you need to install the next library:
- pip install azapi.
"""
import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Linkin Park'
API.title = 'Numb'

API.getLyrics(save=False, ext='lrc')

print(API.lyrics)

