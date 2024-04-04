"""
In order to run this code without error you need to install the next library:
- pip install lyricsgenius.
"""

import lyricsgenius
token = "zU2Vm2ed_USDRB60JfY3fJlGR7yTY5_xZs79iNoCFciHeaJyRviIK7ev_NYDf5U4" #soxinem's token.
genius = lyricsgenius.Genius(token)

def getSong(title,author):
	song = genius.search_song(title, author)
	return song


