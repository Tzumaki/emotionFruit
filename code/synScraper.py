import sys
import re
import json

def regexSubject(todoRegex: list):
    regExp = ""
    filteredWords = []

    for subject in todoRegex:
        regExp = re.findall(r'(\d+)_amr', subject)
        filteredWords.append(regExp)
    
    return filteredWords   

def filterSynset(synsetLines):
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
        # print(todoRegex)
        # print(synsetDis)
        outputWords = regexSubject(todoRegex)

        return outputWords,synsetDis
    else:
        print("Non ci sono synset oggetto :(")
        return 0

def songAssembler(synsnetList, text, id):
    songData = {}
    songData["synset"] = synsnetList
    songData["text"] = text
    songData["id"] = id
    return songData

def synScraper(rdfFile, author, songTitle):
    nqFile = open(rdfFile, "r")
    quadruple = nqFile.readlines()

    countSynWord = 0
    synsetLines = []

    # output of filter
    numVerse_synsets = []
    verses = []
    synsets = []

    for line in quadruple: 
        if "synset" in line:
            synsetLines.append(line)
            countSynWord += 1

    if(countSynWord > 0):
        print(f"synset trovati nel documento: {countSynWord}")
    else:
        exit("Non ci sono synset :(")

    numVerse_synsets = filterSynset(synsetLines)   # list of: list of verses AND list of synsets
    print(f"BOTH{numVerse_synsets}")
    verses = numVerse_synsets[0]
    print(verses)
    synsets = numVerse_synsets[1]
    print(synsets)
        
    # create json file
    '''
    data = {}
    for i, name in enumerate(numVerse_synsets):
        data[name] = synsets[i]
    json_data = json.dumps(data)
    with open("synsetOut.json", "w") as f:
        f.write(json_data)
    '''

    song_dict = {}

    for id_, synset in zip(verses, synsets): # iterate over the lists
        id_val = int(id_[0]) # convert id to integer
        
        if id_val in song_dict:
            song_dict[id_val]["synset"].append(synset)
        else: # create a new entry
            song_dict[id_val] = {
                "synset": [synset],
                "id": id_val
            }

    sorted_songs = sorted(song_dict.values(), key=lambda x: x["id"]) # sort the verses by id
 
    final_object = {"song": sorted_songs, "author": author, "title": songTitle}

    filename = "synScraperOutput.json"

    # save the final object to a separate JSON file
    with open(filename, 'w') as json_file:
        json.dump(final_object, json_file, indent=2)

    print(f"JSON object saved to {filename}")


    nqFile.close()


if __name__ == "__main__":
    if(len(sys.argv)!= 2):
        exit("wrong parameters! \nusage: python synScraper <path_to_file.nq)>")
    synScraper(sys.argv[1])