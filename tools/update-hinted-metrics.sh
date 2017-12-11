#!/bin/env bash
#
# Downloads CacheTT.exe (https://www.microsoft.com/en-us/Typography/tools.aspx)
# and runs it with wine on the built font binaries to generate hdmx, VDMX and
# LTSH tables (precached metrics of glyphs after hinting).
#
# Run from root directory like so: `update-hinted-metrics.sh font.ttf`.

if [ ! -f tools/CacheTT/cachett.exe ]
then
  cd tools
  curl -o FontTools.exe http://download.microsoft.com/download/f/f/a/ffae9ec6-3bf6-488a-843d-b96d552fd815/FontTools.exe
  unzip FontTools.exe
  unzip FontTools/CacheTT.zip
  cd ..
fi

if [[ $1 == *"Ubuntu-C"* ]]
then
  CACHETT_CFG="tools/cachett-configuration-condensed.cfg"
else
  CACHETT_CFG="tools/cachett-configuration.cfg"
fi

wine tools/CacheTT/cachett.exe -V -TVDMX -TLTSH -Thdmx "$1" "$1_" $CACHETT_CFG
mv "$1_" "$1"
