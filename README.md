# emotionFruit
Progetto per il corso di Informatica Umanistica a.a. 2023/2024 \
Corso di Laurea Triennale in Informatica \
Alma Mater Studiorum - Università di Bologna 

Team di sviluppo:
- Elisa Casalini
- Giulia Ferrigno
- Simone Salamone
- Pietro Sami
- Alessandro Tomaiuolo

## Pipeline completa
```
python3 main.py "Autore" "Titolo"
```

## Pipeline a partire da un file .nq
```
python3 main.py -f path/to/nq "Autore" "Titolo"
```
È possibile trovare dei file .nq già salvati nelle cartelle SavedSongs ed extraSongs

## Grafici a partire da JSON
```
python3 main.py -e path/to/json "Autore" "Titolo"
```
È possibile trovare dei file .nq già salvati nella cartella SavedJson

## Prompt ChatGPT 
  
Pretend to be an expert in emotions and return a table with the percentage of the most present emotions among anger, amusement, annoyance, indifference, happiness, inspiration, and sadness in each verse of (song title) by (author).
The output should be a JSON in this format:
```json
{
  "scores": [
    {
      "id": "number",
      "angryscore": "value of anger",
      "amusedscore": "value of amusement",
      "annoyedscore": "value of annoyance",
      "dontcarescore": "value of indifference",
      "happyscore": "value of happiness",
      "inspiredscore": "value of inspiration",
      "sadscore": "value of sadness"
    }
  ]
}
```
for each verse (number), start from zero. the value of scores must be integer, not strings
