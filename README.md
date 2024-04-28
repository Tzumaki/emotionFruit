# PROGETTO INFORMATICA UMANISTICA

## Prompt ChatGPT
```
fingi di essere un esperto di emozioni ritorna una tabella con la percentuale delle più presenti tra rabbia, divertimento, fastidio, indifferenza, felicità ed ispirazione in (titolo canzone) di (autore)
```

## Query SPARQL
In /code runnare:
```
python3 sparql_query.py
```
nota: serve un file synScraperOutput.json popolato

## Output desiderato
```
{
  "song" : [
    {
      "synset" : ["synset1", "synset2"]],
      "text" : "testo",
      "id": numStrofa
    },
    {
      altro oggetto strofa
    }
  ]
  "author" : "Ariana Grande"
  "title" : "One Last Time"
}
```
## Da nq ad array di stringhe
```
python3 synScraper.py ../out.nq
```
Da runnare nella cartella code e dopo aver eseguito lo script di Popi

### Testing

Per testare lo script che ti restituisce il grafo rdf 

```
sh rdf.sh "Nome autore" "Nome canzone"
```

L'output sarà nel file out.nq


### Email professore

Email del professore:

FRED (il testo va prima tradotto in inglese): produce automaticamente un knowledge graph a partire da un testo in inglese. Per annotare le emozioni occorre poi fare una query a Framester.
Esempio:

"Era un mondo adulto, si sbagliava da professionisti"
(Google Translate): "It was an adult world, they made mistakes like professionals"
(FRED: http://wit.istc.cnr.it/stlab-tools/fred/demo/?) : usate l’opzione “Align concepts to Framester” e l’output “Turtle”
(Framester SPARQL engine: http://etna.istc.cnr.it/framester2/sparql) : per ogni disambiguazione nell’output di FRED, interrogate per ottenere l’emotional score, il sentiment score e altro, ex:



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
  
    FILTER (?synset = wn30instances:synset-universe-noun-1)

      } limit 100


Se volete produrre i grafi di FRED in modo programmatico, usate il Machine Reader: https://github.com/anuzzolese/machine-reading , che produrrà quadruple, cioè triple indicizzate con un named graph per ogni frase che passerete al tool secondo le specifiche lì fornite.
A quel punto potete introdurre le query a Framester direttamente nello script che costruirete.
