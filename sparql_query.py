"""
In order to run this code you need to install the next libraries:
- pip install sparqlwrapper
"""
from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template #using for string interpolation

filters = ['wn30:synset-fun-noun-1', 'wn30:supersense-noun_act', 'wn30:synset-mistake-noun-1', 'wn30:synset-fun-noun-1'] #given by the upper level

#remove 'wn30' from the filters
for index, i in enumerate(filters):
    filters[index] = i.replace('wn30:', '')

#specify the DBPedia endpoint
sparql = SPARQLWrapper("http://etna.istc.cnr.it/framester2/sparql")

#repeat the query for every filter
for i in filters:

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
        knowlged = result["results"]["bindings"][0]

        #check if the dict doesn't have the 'angryscore' field in it
        if 'angryscore' in result["results"]["bindings"][0]:
            print("Query for " + i + ":")
            print("Angry: " + knowlged["angryscore"]["value"])
            print("Amused: " + knowlged["amusedscore"]["value"])
            print("Annoyed: " + knowlged["annoyedscore"]["value"])
            print("Don't care: " + knowlged["dontcarescore"]["value"])
            print("Happy: " + knowlged["happyscore"]["value"])
            print("Inspired: " + knowlged["inspiredscore"]["value"])
            print("Sad: " + knowlged["sadscore"]["value"])
            print("End of the query \n")
        else:
            continue
    else:
        continue
"""
for i in result["results"]["bindings"]:
    print(i)
    print("\n")

print("STOP")

"""