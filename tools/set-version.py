#!/bin/env python3
#
# Sets the version number in the UFO metadata and inserts a special version
# glyph that helps with debugging when getting user reports. Reads VERSION.txt
# of the format:
# ```
# 1.234 Some optional text to go into the name table version field
# ```
#
# See http://silnrsi.github.io/FDBP/en-US/Versioning.html for version semantics.
#
# Changing the components or their widths may cause an error during VTT
# compilation. Build the VTT builds and run this script:
# ```
# import fontTools.ttLib
# import vttLib
# import glob
#
# for ttf in glob.glob("source/*ttf"):
#   font=fontTools.ttLib.TTFont(ttf)
#   vttLib.update_composites(font)
#   font.save(ttf)
# ```
# Then redump the VTT source with
# ```
# for f in source/*ttf; do python -m vttLib dump $f ${f/ttf/ufo};done
# ```


import defcon
import glob
import re
import sys

mapping = {'.': 'period', '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
           '9': 'nine'}

versionFormat = re.compile("(\d\.\d\d\d)( [\w ]+)*")

with open("VERSION.txt") as v:
    match = versionFormat.match(v.read().strip())

    if not match:
        print("VERSION.txt must have the format '\d.\d\d\d Optional text'!")
        sys.exit(1)

    version = match.group(1)
    if match.group(2):
        versionExtraInfo = match.group(2)
    else:
        versionExtraInfo = ""

versionFigures = [mapping[x] for x in version]
majorVersion, minorVersion = version.split(".")

for ufo in glob.glob("source/*.ufo"):
    print(ufo)
    font = defcon.Font(ufo)

    # Set metadata
    font.info.versionMajor = int(majorVersion)
    font.info.versionMinor = int(minorVersion)
    font.info.openTypeNameVersion = "Version " + version + versionExtraInfo
    font.info.openTypeNameUniqueID = "{} {} Version {}".format(
        font.info.familyName, font.info.styleName, version)

    # Insert version glyph
    versionGlyph = defcon.Glyph()
    versionGlyph.unicode = 0xEFFD
    advanceWidth = 0

    if not "Mono" in ufo:
        for figure in versionFigures:
            if "period" in figure:
                glyph = figure
            else:
                glyph = figure + "inferior"
            c = defcon.Component()
            c.baseGlyph = glyph
            c.transformation = (1, 0, 0, 1, advanceWidth, 0)
            advanceWidth += font[glyph].width
            versionGlyph.appendComponent(c)
    else:
        c1 = defcon.Component()
        c1.baseGlyph = versionFigures[0] + ".sups"
        c1.transformation = (1, 0, 0, 1, -150, 0)
        versionGlyph.appendComponent(c1)
        c2 = defcon.Component()
        c2.baseGlyph = versionFigures[2] + ".sups"
        c2.transformation = (1, 0, 0, 1, 150, 0)
        versionGlyph.appendComponent(c2)
        c3 = defcon.Component()
        c3.baseGlyph = versionFigures[3] + ".sinf"
        c3.transformation = (1, 0, 0, 1, -150, 0)
        versionGlyph.appendComponent(c3)
        c4 = defcon.Component()
        c4.baseGlyph = versionFigures[4] + ".sinf"
        c4.transformation = (1, 0, 0, 1, 150, 0)
        versionGlyph.appendComponent(c4)
        advanceWidth = 500

    versionGlyph.width = advanceWidth

    font.insertGlyph(versionGlyph, "uniEFFD")
    font.save(ufo)
