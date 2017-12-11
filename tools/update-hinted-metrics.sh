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

CACHETT_CFG="tools/cachett-configuration.cfg"

# The condensed face and the Mono fonts use different parameters:
# 1) VDMX: cache values for sizes up to 255, only calculate for a 1:1 ratio.
# 2) hdmx: the condensed face caches for fewer ppems.
if [[ $1 == *"Ubuntu-C"* ]]
then
  CACHETT_CFG="tools/cachett-configuration-condensed.cfg"
elif [[ $1 == *"UbuntuMono"* ]]
then
  CACHETT_CFG="tools/cachett-configuration-mono.cfg"
fi

# The Google Fonts version of Mono-BI does not ship with a VDMX table. As there
# are no htmx or LTSH tables in the Mono fonts, we can go home now.
if [[ $1 == *"UbuntuMono-BI"* ]]
then
  exit 0
fi

wine tools/CacheTT/cachett.exe -V -TVDMX -TLTSH -Thdmx "$1" "$1_" $CACHETT_CFG
mv "$1_" "$1"
