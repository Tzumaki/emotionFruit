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

def filterSynSet(synsetLines: list):
    outputWords = []
    todoRegex = []
    countSynSubj = 0
    synsetDis = []
    
    for synLine in synsetLines:
        singleTag = synLine.split(" ") #divido la quadupla nei 4 elementi
           
        if "synset" in singleTag[2]: #se l'oggetto della quadrupla ha synSet
            todoRegex.append(singleTag[0]) #aggiungo il soggetto alla lista su cui farema la regex
            s = str(singleTag[2]).split("/")
            sysToappend = s[len(s)-1]
            synsetDis.append(sysToappend[:len(sysToappend)-1])
            countSynSubj += 1

    if(countSynSubj > 0):
        print(f"synset oggetto totali: {countSynSubj}")
        print(todoRegex)
        print(synsetDis)
        outputWords = regexSubject(todoRegex)
        return outputWords,synsetDis
    else:
        print("Non ci sono synset oggetto :(")
        return 0



if __name__ == "__main__":
    if(len(sys.argv)!= 2):
        exit("wrong parameters! \nusage: python synScraper <path_to_file.nq)>")

    nqFile = open(sys.argv[1], "r")

    quadruple = nqFile.readlines()
    countSynWord = 0
    synsetLines = []
    words = []

    for line in quadruple: 
        if "synset" in line:
            synsetLines.append(line)
            countSynWord += 1

    if(countSynWord > 0):
        print(f"synset trovati nel documento: {countSynWord}")
    else:
        exit("Non ci sono synset :(")

    words = filterSynSet(synsetLines)   #lista di liste di parole associate al synSet
    synsets = words[1]
    words = words[0]

    finalList = [element for sublist in words for element in sublist]
    print(finalList) #liste di parole associate al synSet
        
    # crea il file json
    data = {}
    for i, name in enumerate(finalList):
        data[name] = synsets[i]
    json_data = json.dumps(data)
    with open("synsetOut.json", "w") as f:
        f.write(json_data)

    nqFile.close()