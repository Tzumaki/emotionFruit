import pandas as pd
from lyrics_from_title_genius import getSong
import sys
import re


def parseText(Lyrics):
    regex1 = re.compile("\[(.*?)\]", flags=re.VERBOSE)
    regex2 = re.compile("\d+\s*.*Lyrics?",flags= re.VERBOSE)
    regex3 = re.compile("\d+\s*.*Embed?",flags=re.VERBOSE)
    parsedLyrics = regex1.sub("",Lyrics)
    parsedLyrics = regex2.sub("",parsedLyrics);
    parsedLyrics = regex3.sub("",parsedLyrics);
    return parsedLyrics.split("\n\n")


dict = {'corpus_id':[],'document_id':[],'sentence_id':[],'content':[]}
song = getSong(sys.argv[1],sys.argv[2])

for indice,strofa in enumerate(parseText(song.lyrics)):
    if(strofa.replace("\n"," ").replace(",","")): 
        dict['corpus_id'].append(song.title)
        dict['document_id'].append(1)
        dict['sentence_id'].append(indice)
        dict['content'].append(strofa.replace("\n"," ").replace(",",""))

df = pd.DataFrame(dict)
print(df)
df.to_csv('out.csv', sep=";",index=False) 
    







