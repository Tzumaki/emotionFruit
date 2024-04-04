import pandas as pd
from lyrics_from_title_genius import getSong


song = getSong("Runaway","Kanye West")
text = song.lyrics.split("\n\n")

dict = {'corpus_id':[],'document_id':[],'sentence_id':[],'content':[]}

for indice,strofa in enumerate(text):
    dict['corpus_id'].append(song.title)
    dict['document_id'].append(1)
    dict['sentence_id'].append(indice)
    dict['content'].append(strofa)


df= pd.DataFrame(dict)
print(df)

df.to_csv('out.csv', sep=";",index=False) 
    


    











