"""
In order to run this code you need to install the next libraries:
- pip install sparqlwrapper
"""
from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template #using for string interpolation
import json 

#Expected synScraperOutput.json
"""
data = {"song": [
            {"synset": ["synset-again-adverb-1", "synset-alone-adjectivesatellite-3", "synset-entirely-adverb-2", "synset-friend-noun-1", "synset-intoxicated-adjective-1", "synset-layer-noun-1", "synset-phone-noun-2", "synset-thinker-noun-1", "synset-time-noun-1", "synset-besides-adverb-2", "synset-many-adjective-1", "synset-back-adverb-1", "synset-nowadays-adverb-1", "synset-back-adverb-2", "synset-convention-noun-2", "synset-still-adverb-1", "synset-baby-noun-5"], 
             "text": "Lorem ipsum dolor sit amet", 
             "id": 1}
         ],
         "author": "Dua Lipa",
         "title": "New Rules"
}
"""

def checkValues(scores):
    atLeastOneValue = False

    for key in scores:
        if key != "id" and key != "text":
            if scores[key] != 0:
                atLeastOneValue = True

    return atLeastOneValue

def percentage(emotions):
    total = 0
    percentages = emotions.copy()

    for key in emotions:
        if key != "id" and key != "text":
            total += emotions[key]

    for key in percentages:
        if key != "id" and key != "text":
            # x = value*100 / total
            percentages[key] = emotions[key] * 100 / total

    print("Array of percentages:")
    print(percentages)
    return percentages
    


listOfValues = []

def sparql_query(withText):
    f = open('synScraperOutput.json')
    data = json.load(f)
    f.close()


    finalResults = {"title": data["title"], "author": data["author"], 
                    "scores": []}

    for verse in range(len(data["song"])):

        #remove 'wn30' from the filters
        for index, i in enumerate(data["song"][verse]["synset"]):
            data["song"][verse]["synset"][index] = i.replace('wn30:', '')

        #specify the DBPedia endpoint
        sparql = SPARQLWrapper("http://etna.istc.cnr.it/framester2/sparql")

        score = {}
        #init
        if withText:
            score = {
                "id": data["song"][verse]["id"], 
                "text": data["song"][verse]["text"],
                "angryscore": 0, "amusedscore": 0, "annoyedscore": 0, "dontcarescore": 0, "happyscore": 0, "inspiredscore": 0, "sadscore": 0}
        else:
            score = { 
                "id": data["song"][verse]["id"], 
                "angryscore": 0, "amusedscore": 0, "annoyedscore": 0, "dontcarescore": 0, "happyscore": 0, 
                "inspiredscore": 0, "sadscore": 0}
            
        #repeat the query for every filter
        for i in data["song"][verse]["synset"]:

            #filter interpolation
            template = Template("""
                SELECT DISTINCT ?frame ?synset ?gloss ?domain ?proxhyponym ?tophyponym ?d0 ?posscore ?negscore ?amusedscore ?angryscore ?annoyedscore ?dontcarescore ?happyscore ?inspiredscore ?sadscore ?agenttrope ?undergoertrope ?simil ?othersense

            WHERE {

            ?frame rdf:type <https://w3id.org/framester/schema/ConceptualFrame> , owl:Class ;

            rdfs:subClassOf <https://w3id.org/framester/schema/FrameOccurrence> ;

            owl:sameAs ?fnframe .

            OPTIONAL {?fnframe skos:closeMatch ?synset}

            OPTIONAL {?synset <https://w3id.org/framester/wn/wn30/schema/gloss> ?gloss}

            OPTIONAL {?synset <https://w3id.org/framester/wn/wn30/wndomains/synsetDomain> ?domain}

            OPTIONAL {?synset <http://www.ontologydesignpatterns.org/ont/own3/own2dul.owl#proxhyp> ?proxhyponym}

            OPTIONAL {?synset <http://www.ontologydesignpatterns.org/ont/own3/own2dul.owl#hyp> ?tophyponym}

            OPTIONAL {?synset <http://www.ontologydesignpatterns.org/ont/own3/own2dul.owl#d0> ?d0}

            OPTIONAL {?synset <https://w3id.org/framester/sentiwordnet/posScore> ?posscore}

            OPTIONAL {?synset <https://w3id.org/framester/sentiwordnet/negScore> ?negscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/AMUSEDscore> ?amusedscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/ANGRYscore> ?angryscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/ANNOYEDscore> ?annoyedscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/DONT_CAREscore> ?dontcarescore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/HAPPYscore> ?happyscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/INSPIREDscore> ?inspiredscore}

            OPTIONAL {?synset <https://w3id.org/framester/depechemood/depechemood2wn/SADscore> ?sadscore}

            OPTIONAL {?synset <https://w3id.org/framester/wn/wn30/verbnounsynsettropes/agent> ?agenttrope}

            OPTIONAL {?synset <https://w3id.org/framester/wn/wn30/verbnounsynsettropes/undergoer> ?undergoertrope}

            OPTIONAL {?synset <https://w3id.org/framester/wn/wn30/schema/derivationallyBasedSynsetSimilarity> ?simil}

            OPTIONAL {?synset owl:sameAs ?othersense}

            FILTER (?synset = wn30instances:$filter)

            } limit 100
            """)

            #single query
            sparql.setQuery(template.substitute(filter = i))

            #convert results to JSON format
            sparql.setReturnFormat(JSON)
            result = sparql.query().convert()

            #check if the result isn't empty
            if(result["results"]["bindings"]):
                knowledge = result["results"]["bindings"][0]

                #check if the dict doesn't have the 'angryscore' field in it
                if 'angryscore' in result["results"]["bindings"][0]:
                    #print("Query for " + i + ":")
                    #print("Angry: " +   knowledge["angryscore"]["value"])
                    #print("Amused: " +  knowledge["amusedscore"]["value"])
                    #print("Annoyed: " + knowledge["annoyedscore"]["value"])
                    #print("Don't care: " +  knowledge["dontcarescore"]["value"])
                    #print("Happy: " +   knowledge["happyscore"]["value"])
                    #print("Inspired: " +    knowledge["inspiredscore"]["value"])
                    #print("Sad: " + knowledge["sadscore"]["value"])
                    #print("End of the query \n")

                    score["angryscore"] += float(knowledge["angryscore"]["value"])
                    score["amusedscore"] += float(knowledge["amusedscore"]["value"])
                    score["annoyedscore"] += float(knowledge["annoyedscore"]["value"])
                    score["dontcarescore"] += float(knowledge["dontcarescore"]["value"])
                    score["happyscore"] += float(knowledge["happyscore"]["value"])
                    score["inspiredscore"] += float(knowledge["inspiredscore"]["value"])
                    score["sadscore"] += float(knowledge["sadscore"]["value"])

                else:
                    continue
            else:
                continue

        if checkValues(score):
            finalResults["scores"].append(score)
            #TODO: RITORNARE PERCENTUALI NEL FINAL RESULTS
            percentage(score)


    print(finalResults)
    return finalResults


if __name__ == "__main__":
    sparql_query()



"""
Il debug pazzo di Simone

for i in result["results"]["bindings"]:
    print(i)
    print("\n")

print("STOP")

"""