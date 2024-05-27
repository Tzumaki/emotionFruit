import sys
import re
import json
import csv


def countSynsets(quadruple: list):
    countSynWord = 0
    synsetLines = []

    for line in quadruple: 
        if "synset" in line:
            synsetLines.append(line)
            countSynWord += 1

    if(countSynWord > 0):
        print(f"synset trovati nel documento: {countSynWord}")
    else:
        exit("Non ci sono synset :(")
    return synsetLines


def regexSubject(todoRegex: list):
    regExp = ""
    filteredWords = []

    for subject in todoRegex:
        regExp = re.findall(r'(\d+)_amr', subject)
        filteredWords.append(regExp)
    
    return filteredWords   


def filterSynset(synsetLines: list):
    outputWords = [] # numVerse
    todoRegex = [] # subjWithNumVerse
    synsetDis = [] # objWithSynset
    countSynSubj = 0
    
    for synLine in synsetLines:
        singleTag = synLine.split(" ") # divide the quaduple in the 4 elements
           
        if "synset" in singleTag[2]: # if the object of the quadruple has a synSet
            todoRegex.append(singleTag[0]) # add the subject to the list where we'll do the regex

            # to extrapolate the synset of the object
            s = str(singleTag[2]).split("/")
            sysToappend = s[len(s)-1]
            synsetDis.append(sysToappend[:len(sysToappend)-1]) # append most recent sys

            countSynSubj += 1

    if(countSynSubj > 0):
        print(f"synset oggetto totali: {countSynSubj}")
        outputWords = regexSubject(todoRegex)

        return outputWords,synsetDis
    else:
        print("Non ci sono synset oggetto :(")
        return 0


def extractTextCsv():
    with open('out.csv', mode='r') as outCsv:
        allTextCsv = []
        csvReader = csv.reader(outCsv, delimiter=';', skipinitialspace=True)
        header = []
        header = next(outCsv) # skip the fields row

        for row in csvReader:
            allTextCsv.append(row[3]) # append the content
        return allTextCsv


def createDict(allTextCsv: list, verses: list, synsets: list, checkCSV: bool):
    songDictionary = {} # create json file using the following dictionary

    for verse, synset in zip(verses, synsets): # iterate over the lists
        intVerse = int(verse[0]) # convert id to integer
        
        if intVerse in songDictionary:
            songDictionary[intVerse]["synset"].append(synset)
        elif not checkCSV: # json without csv
            songDictionary[intVerse] = {
                "synset": [synset],
                "id": intVerse
            }
        else: # json with csv
            songDictionary[intVerse] = {
                "synset": [synset],
                "id": intVerse,
                "text": allTextCsv[intVerse]
            }
    sortedDict = sorted(songDictionary.values(), key=lambda x: x["id"]) # sort the verses by id
    return sortedDict


def createJson(songDict: dict, author: str, songTitleClean:str):
    finalObject = {"song": songDict, "author": author, "title": songTitleClean}
    filename = "synScraperOutput.json"

    # save the final object to a separate JSON file
    with open(filename, 'w') as jsonFile:
        json.dump(finalObject, jsonFile, indent=2)

    print(f"JSON object saved to {filename}")

def synScraper(rdfFile, author, songTitle, checkCSV):

    nqFile = open(rdfFile, "r")
    quadruple = nqFile.readlines()
    

    # structures for filter
    synsetLines = []
    verseAndSynsets = []
    verses = []
    synsets = []

    synsetLines = countSynsets(quadruple)
    verseAndSynsets = filterSynset(synsetLines)   # list of: list of verses AND list of synsets
    verses = verseAndSynsets[0]
    synsets = verseAndSynsets[1]


    # structures for json
    allTextCsv = []
    songDict = {}

    if(checkCSV):
        allTextCsv = extractTextCsv() # list of lyrics by verse
    
    songDict = createDict(allTextCsv, verses, synsets, checkCSV)

    songTitleClean = songTitle.replace("_", " ")
    createJson(songDict, author, songTitleClean)


    nqFile.close()


if __name__ == "__main__":
    if(len(sys.argv)!= 2):
        exit("wrong parameters! \nusage: python synScraper <path_to_file.nq)>")
    synScraper(sys.argv[1])
