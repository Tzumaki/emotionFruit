"""
In order to run this code without error you need to install the next library:
- pip install lyricsgenius.
"""
import lyricsgenius
token = "zU2Vm2ed_USDRB60JfY3fJlGR7yTY5_xZs79iNoCFciHeaJyRviIK7ev_NYDf5U4"
genius = lyricsgenius.Genius(token)

#artist = genius.search_artist("Taylor Swift")
#song = artist.song("Blank Space")
# or:
song = genius.search_song("Blank Space", "Taylor Swift")
print(song.lyrics)

