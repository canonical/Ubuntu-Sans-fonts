#!/bin/env python2
#
# Redumps the VTT source to the UFO. Needed when e.g. the version glyphs are
# updated and offsets change.


import fontTools.ttLib
import vttLib
import glob

for ttf in glob.glob("source/*ttf"):
    ufo = ttf.replace("ttf", "ufo")
    print("Updating VTT code for {}.".format(ufo))

    font = fontTools.ttLib.TTFont(ttf)
    vttLib.update_composites(font)
    font.save(ttf)
    vttLib.vtt_dump(ttf, ufo)
