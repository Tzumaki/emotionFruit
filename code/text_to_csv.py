import pandas as pd
from lyrics_from_title_lyrist import getSong
import sys
import re

outputFile = "out.csv"

def parseText(Lyrics):
    regex1 = re.compile("\[(.*?)\]", flags=re.VERBOSE) #Elimina tutte le parti tra parentesi
    parsedLyrics = regex1.sub("",Lyrics);
    return parsedLyrics.split("\n\n")

def createCSV(author,song):
    dict = {'corpus_id':[],'document_id':[],'sentence_id':[],'content':[]}
    songObject = getSong(author,song)
    arrayStrofe = []
    indice = 0
    for i,strofa in enumerate(parseText(songObject["lyrics"])):
        if(strofa.replace("\n"," ").replace(",","")): 
            dict['corpus_id'].append(songObject["title"].replace(" ","_"))
            dict['document_id'].append(1)
            dict['sentence_id'].append(indice)
            dict['content'].append(strofa.replace("\n"," ").replace(",",""))
            arrayStrofe.append(strofa.replace("\n"," ").replace(",",""))
            indice = indice + 1 
    df = pd.DataFrame(dict)
    df.to_csv(outputFile, sep=";",index=False) 
    return outputFile, arrayStrofe, songObject["artist"], songObject["title"].replace(" ","_")
    

if __name__ == "__main__":
    createCSV(sys.argv[1],sys.argv[2])






