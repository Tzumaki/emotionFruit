#!/bin/bash
echo "save Json and launch draw-chart subroutine"
read -p "Author: " author
read -p "Song ": song
touch "SavedJson/${song}.json"

echo "Paste the Json, the press Ctrl-D to close the output"
cat > "SavedJson/${file_name}.json"

python3 main.py -e "SavedJson/${file_name}.json" "$author" "$song"
