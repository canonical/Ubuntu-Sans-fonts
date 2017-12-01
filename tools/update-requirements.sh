#!/bin/env bash
#
# Updates the requirements.txt file. Is run from the Makefile and must run on
# the top-level.
#
# Update the script when font production relies on more than fontmake and
# vttLib.

set -e # Fail immediately when any command does.

if [ ! -f requirements.txt ]
then
  echo "This script must be run in the same directory that contains the \
requirements.txt file."
  exit 1
fi

TMPDIR=$(mktemp -d)
python3 -m venv $TMPDIR
source $TMPDIR/bin/activate

pip3 install \
  ufo2ft \
  --find-links https://github.com/daltonmaag/vttLib/releases vttLib
pip3 freeze -r requirements.txt \
  | grep -v "were added by pip freeze" > new_requirements.txt
mv new_requirements.txt requirements.txt
