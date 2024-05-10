import sys
sys.path.append("./code/")
import os
from text_to_csv import createCSV
from synScraper import synScraper
from sparql_query import sparql_query
from emotionsChart import drawCharts
import subprocess


if __name__ == "__main__":
    if(len(sys.argv) == 2 and sys.argv[1] == "--help"):
        exit('usage: \n\tpython main.py "Author" "Song" ')
    if(len(sys.argv)!= 3):
        exit("wrong parameters!")
    

    author = sys.argv[1]
    songTitle = sys.argv[2]
    outputFile = createCSV(author,songTitle)
    process = subprocess.run(["sh","rdf.sh"] + [outputFile])
    synScraper("out.nq")
    listOfEmotions = sparql_query()
    print(listOfEmotions)
    drawCharts(listOfEmotions, author, songTitle)
