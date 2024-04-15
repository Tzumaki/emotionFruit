import sys
import re

def regexSubject(todoRegex: list):
    regExp = ""
    filredWords = []
    for subject in todoRegex:
        regExp = re.findall(r'/([^/<>]+)>', subject)
        filredWords.append(regExp)
    return filredWords   

def filterSynSet(synsetLines: list):
    outputWords = []
    todoRegex = []
    countSynSubj = 0
    
    for synLine in synsetLines:
        singleTag = synLine.split(" ") #divido la quadupla nei 4 elementi
           
        if "synset" in singleTag[2]: #so l'oggetto della quadrupla ha synSet
            print(singleTag[0]) #aggiumgo il soggetto alla lista su cui farema la regex
            todoRegex.append(singleTag[0])
            countSynSubj += 1

    if(countSynSubj > 0):
        print(f"Tot synset oggetto: {countSynSubj}")
    else:
        print("Non ci sono synset oggetto :(")

    print(todoRegex)
    outputWords = regexSubject(todoRegex)
    return outputWords

if __name__ == "__main__":

    nqFile = open(sys.argv[1], "r")
    quadruple = nqFile.readlines()

    countSynWord = 0
    synsetLines = []
    words = []

    for line in quadruple: 
        if "synset" in line:
            synsetLines.append(line)
            countSynWord += 1

    words = filterSynSet(synsetLines) #lista di liste di parole associate al synSet

    finalList = [element for sublist in words for element in sublist]
    print(finalList) #liste di parole associate al synSet

    if(countSynWord > 0):
        print(f"Tot synset nel doc: {countSynWord}")
    else:
        print("Non ci sono synset :(")
        

    nqFile.close()