import matplotlib.pyplot as plt
from bubbleChart import drawBubbles

LABELS =  ["angry", "amused", "annoyed","dont care", "happy", "inspired","sad"]
COLORS = ['red', 'pink', 'grey', 'purple', 'orange', 'green', 'blue']
totalScores = [0,0,0,0,0,0,0]

def drawCharts(data, author, song):
    length = len(data["scores"])
    print(length)
    listOfScores = []

    fig, axs = plt.subplots(length)
    fig.suptitle("Emotions of " + song + " compared to the verses by " + author)

    for i in range(0, length):
        listOfEmotions = list(data["scores"][i].items()) #get the scores and remove the id
        listOfEmotions = listOfEmotions[1:]
        print(listOfEmotions)

        counter = 0
        for tup in listOfEmotions: #get a list of values for each emotions
            listOfScores.append(tup[1])
            totalScores[counter] += tup[1]
            counter += 1

        if sum(listOfScores) != 0:  # Check if the sum of the list is not zero
            axs[i].pie(listOfScores, labels=LABELS, colors = COLORS)
            axs[i].set_title("verse n. "+ str(i+1))
        listOfScores.clear()

    plt.show()
    drawBubbles(totalScores)

if __name__ == "__main__":
    data = {'scores': [{'id': 0, 'angryscore': 0, 'amusedscore': 0, 'annoyedscore': 0, 'dontcarescore': 0, 'happyscore': 0, 'inspiredscore': 0, 'sadscore': 0}, {'id': 1, 'angryscore': 0, 'amusedscore': 0, 'annoyedscore': 0, 'dontcarescore': 0, 'happyscore': 0, 'inspiredscore': 0, 'sadscore': 0}, {'id': 2, 'angryscore': 0, 'amusedscore': 0, 'annoyedscore': 0, 'dontcarescore': 0, 'happyscore': 0, 'inspiredscore': 0, 'sadscore': 0}, {'id': 3, 'angryscore': 0.38662, 'amusedscore': 0.1834709, 'annoyedscore': 0.0199918, 'dontcarescore': 0.38682500000000003, 'happyscore': 0.27270700000000003, 'inspiredscore': 0.26410900000000004, 'sadscore': 0.0815309}, {'id': 5, 'angryscore': 0, 'amusedscore': 0, 'annoyedscore': 0, 'dontcarescore': 0, 'happyscore': 0, 'inspiredscore': 0, 'sadscore': 0}, {'id': 6, 'angryscore': 0, 'amusedscore': 0, 'annoyedscore': 0, 'dontcarescore': 0, 'happyscore': 0, 'inspiredscore': 0, 'sadscore': 0}]}
    drawCharts(data, "Pixies", "Hey")
