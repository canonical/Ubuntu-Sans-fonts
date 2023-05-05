#!/bin/zsh
ttfPath="../fonts/ttf"
referenceFontPath="../fonts/ttf/Ubuntu-Regular.ttf"
for file in $ttfPath/*; do 
    ttfautohint $file ${file//.ttf/-hinted.ttf} -R $referenceFontPath
    echo hinted $file
done