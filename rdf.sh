#!/bin/bash

cd code

if python3 text_to_csv.py $1 $2 ; then
    echo "Generato file .csv"
else
    echo "Qualcosa è andato storto, riprova"
fi

cd ..

if cd machine-reading; then
    echo "Entering machine-reading directory"
else
    git clone --filter=blob:none --quiet https://github.com/anuzzolese/machine-reading;
fi

pip install .
python3 mr.py -m amr2fred -d ';' -n 'https://w3id.org/stlab/mr_data/' -o ../out.nq ../code/out.csv 


