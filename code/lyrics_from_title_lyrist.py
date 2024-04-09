"""
Please notice that this API (lyrist) permits only 150 per hour.
"""

import requests
from string import Template #using for string interpolation

track = "Sere Nere"
artist = "Tiziano Ferro"

#track and artist interpolation
template = Template("https://lyrist.vercel.app/api/:$track/:$artist")
url = template.substitute(track = track, artist = artist)

response = requests.get(url)
data = response.json()

print(data["lyrics"])