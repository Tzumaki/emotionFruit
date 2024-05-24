import sys
sys.path.append("./code/")
import os
from text_to_csv import createCSV
from synScraper import synScraper
from sparql_query import sparql_query
import subprocess
savedSongsDirectory = "SavedSongs/" 


if __name__ == "__main__":
    if(len(sys.argv)>3):
        exit("wrong parameters!")
        
    songTitle = sys.argv[1]
    author = sys.argv[2] if len(sys.argv)==3 else "" 
    outputFile,arrayStrofe,author, songTitle = createCSV(author,songTitle)
    process = subprocess.run(["sh","rdf.sh"] + [outputFile, songTitle])
    synScraper(savedSongsDirectory + songTitle+ ".nq" )
    sparql_query()
