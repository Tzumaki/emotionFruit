import sys
sys.path.append("./code/")
import os
from text_to_csv import createCSV
from synScraper import synScraper
from sparql_query import sparql_query
from emotionsChart import drawCharts, drawChartsFromJson
import subprocess  
savedSongsDirectory = "SavedSongs/" 
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get the emotions from a song's text")
    parser.add_argument('Author', metavar='Author', type=str, help="Song's author")
    parser.add_argument('Title', metavar='Title', type=str, help="Song's title")
    parser.add_argument('--file', '-f', type=str, help="Optional input .nq file")
    parser.add_argument('--emotions', '-e',type=str, help="Optional input json emotions")

    args = parser.parse_args()
    
    author = args.Author
    songTitle = args.Title

    if args.emotions:
        drawChartsFromJson(args.emotions, author, songTitle)
        exit("Reading json end succesfully")
    elif args.file:
        if os.path.isfile(args.file) and str(args.file).endswith('.nq'):
            synScraper(args.file, author, songTitle)
        else:
            exit("file does not exist or wrong file format")
    else:
        outputFile,arrayStrofe,author, songTitle = createCSV(author,songTitle)
        process = subprocess.run(["sh","rdf.sh"] + [outputFile, songTitle])
        synScraper(savedSongsDirectory + songTitle+ ".nq", author, songTitle)

    listOfEmotions = sparql_query()
    print(listOfEmotions)
    drawCharts(listOfEmotions, author, songTitle)
