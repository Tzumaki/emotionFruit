import matplotlib.pyplot as plt
from bubbleChart import drawBubbles
import json

LABELS =  ["angry", "amused", "annoyed", "dont care", "happy", "inspired", "sad"]
COLORS = ["red", "pink", "grey", "purple", "orange", "green", "blue"]
totalScores = [0, 0, 0, 0, 0, 0, 0]



def drawLines(allSongScores):
    lines = list(range(0,len(allSongScores)))
    print(allSongScores)

    for i in range(0, len(LABELS)):
        printableScores = [item[i] for item in allSongScores] #take the first element for each sublist
        plt.plot(lines,printableScores, label=LABELS[i], color=COLORS[i])
    
    plt.xlabel("verse")
    plt.ylabel("score")
    plt.legend()
    plt.show()


def drawCharts(data, author, song):
    length = len(data["scores"])
    print(length)
    listOfScores = []
    allSongScores = []

    fig, axs = plt.subplots(length)
    fig.suptitle("Emotions of " + song + " by " + author)

    if length == 1:
        axs = [axs]

    for i in range(0, length):
        listOfEmotions = list(data["scores"][i].items()) # get the scores and the id
        id = listOfEmotions[0]
        id = id[1]
        listOfEmotions = listOfEmotions[1:]

        counter = 0
        for tup in listOfEmotions: # get a list of values for each emotions
            listOfScores.append(tup[1]) 
            totalScores[counter] += tup[1] # this is for the bubblechart, save the total
            counter += 1

        print(listOfScores)
        allSongScores.append(listOfScores.copy())

        if sum(listOfScores) != 0:  # Check if the sum of the list is not zero
            axs[i].pie(listOfScores, labels=None, colors =COLORS)
            axs[i].set_title("verse n. "+ str(id))
        listOfScores.clear()

    plt.legend(LABELS)
    plt.show()
    drawBubbles(totalScores)
    drawLines(allSongScores)

def drawChartsFromJson(file, author, song):
    f = open(file)
    emotions = json.load(f)
    f.close()

    drawCharts(emotions, author, song)

if __name__ == "__main__":
    data = {'scores': [{'id': 3, 'angryscore': 0.38662, 'amusedscore': 0.1834709, 'annoyedscore': 0.0199918, 'dontcarescore': 0.38682500000000003, 'happyscore': 0.27270700000000003, 'inspiredscore': 0.26410900000000004, 'sadscore': 0.0815309}]}
    drawCharts(data, "Pixies", "Hey")
