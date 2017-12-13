#!/bin/env python3
#
# This is a hack to change the hdmx table widths for the uniF000 debug glyph to
# zero against CacheTT's better judgment. Why? Because the Google Fonts release
# (specifically BI, LI, MI and M) has the fields set to zero. REMOVE THIS ONCE
# IT HAS BEEN PROVEN UNNECESSARY.

import argparse
import fontTools.ttLib

parser = argparse.ArgumentParser()
parser.add_argument("ttf", type=str, help="The path to the TTF to be modified.")
args = parser.parse_args()

# This only needs to be done in BI, LI, MI and M.
if any(x in args.ttf for x in ("BI", "LI", "MI", "M")):
    ttf = fontTools.ttLib.TTFont(args.ttf)

    # The values can't be changed through the proper accessor methods, so access
    # private fields directly.
    for index, table in ttf["hdmx"].hdmx.items():
        table._array[table._map["uniF000"]] = 0

    del ttf["LTSH"].yPels["uniF000"]

    ttf.save(args.ttf)
