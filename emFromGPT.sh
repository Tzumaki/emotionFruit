#!/bin/bash
echo "Save Json and launch draw-chart subroutine"
echo "Write the title with underscores in between words"
read -p "Author: " author
read -p "Song: " song
touch "SavedJson/${song}.json"

echo "Paste the Json, then press Ctrl-D to close the output"
cat > "SavedJson/${song}.json"

python3 main.py -e "SavedJson/${song}.json" "$author" "$song"
