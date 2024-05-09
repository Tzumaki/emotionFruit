import sys
sys.path.append("./code/")
import os
from text_to_csv import createCSV
from synScraper import synScraper
from sparql_query import sparql_query
import subprocess


if __name__ == "__main__":
    if(len(sys.argv)!= 3):
        exit("wrong parameters!")

    author = sys.argv[1]
    songTitle = sys.argv[2]
    outputFile = createCSV(author,songTitle)
    process = subprocess.run(["sh","rdf.sh"] + [outputFile])
    #Passare a synScraper un array con le strofe del testo per formattare correttamente il json risultante ("text" o "lyrics": "Lorem ipsum bla bla bla")
    synScraper("out.nq", author, songTitle)
    sparql_query()
