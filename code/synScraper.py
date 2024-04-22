import sys
import re
import json

def regexSubject(todoRegex: list):
    regExp = ""
    filredWords = []
    for subject in todoRegex:
        regExp = re.findall(r'/([^/<>]+)>', subject)
        filredWords.append(regExp)
    return filredWords   

# ritorna il numero della strofa
def getVerseId(line):
    versePlusTitle = line.split("/")
    return int( \
                (versePlusTitle[len(versePlusTitle)-2]\
                .split("_"))[2]\
            )

def filterSynSet(synsetLines: list):
    countSynSubj = 0
    verses = {}
    
    for synLine in synsetLines:
        singleTag = synLine.split(" ") # divido la quadupla nei 4 elementi
           
        if "synset" in singleTag[2]:    # se l'oggetto della quadrupla ha synSet come predicato
            verseId = getVerseId(singleTag[0])

            # divido l'elemento e prendo l'identificativo del synset
            s = str(singleTag[2]).split("/")
            sysToappend = s[len(s)-1]

            try :
                verses[verseId].append(sysToappend[:len(sysToappend)-1])
            except:
                verses[verseId] = [sysToappend[:len(sysToappend)-1]]

            countSynSubj += 1

    if(countSynSubj > 0):
        """TODO: CONTROLLARE IL DIZIONARIO ORDINATO"""
        print(f"synset oggetto totali: {countSynSubj} \n {verses}")
        sorted_dict = dict(sorted(verses.items(), key=lambda x:x[0]))
        print(sorted_dict)
        return verses 
    else:
        print("Non ci sono synset oggetto :(")
        return 0

def songAssembler(synsnetList, text, id):
    songData = {}
    songData["synset"] = synsnetList
    songData["text"] = text
    songData["id"] = id
    return songData

if __name__ == "__main__":
    if(len(sys.argv)!= 2):
        exit("wrong parameters! \nusage: python synScraper <path_to_file.nq)>")
    # leggiamo le righe del file .nq
    quadruple = []
    with open(sys.argv[1], "r") as nqF:
        quadruple = nqF.readlines()

    countSynWord = 0
    synsetLines = []
    #filtriamo solo le parole con synset
    for line in quadruple: 
        if "synset" in line:
            synsetLines.append(line)
            countSynWord += 1

    if(countSynWord > 0):
        print(f"synset trovati nel documento: {countSynWord}")
    else:
        exit("Non ci sono synset :(")

    # dizionario con verso : [lista di synset]
    synsetsInVerse = filterSynSet(synsetLines)
    
    # crea il file json
    finalJson = {}
    song = []
    for key in synsetsInVerse.keys():
        song.append(songAssembler(synsetsInVerse[key], "Lorem", key))
    finalJson["song"] = song
    finalJson["author"] = "Aldo"
    finalJson["title"] = "Gangemi"

    json_data = json.dumps(finalJson)
    with open("synsetOut.json", "w") as f:
        f.write(json_data)