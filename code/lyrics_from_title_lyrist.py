"""
Please notice that this API (lyrist) permits only 150 per hour.
"""

import requests
from string import Template #using for string interpolation


def getSong(title,author):
    #track and artist interpolation
    template = Template("https://lyrist.vercel.app/api/:$track/:$artist")
    url = template.substitute(track = title, artist = author)

    response = requests.get(url)
    data = response.json()
    return data
