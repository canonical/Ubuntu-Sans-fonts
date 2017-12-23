import sys
import logging
import defcon
import ufo2ft
import vttLib
import argparse
import fontTools.ttLib


logger = logging.getLogger(__file__)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("ufo", type=str, help="The path to the input UFO.")
    parser.add_argument("ttf", type=str, help="The path to the output TTF.")
    args = parser.parse_args()

    logging.basicConfig(level="INFO")

    ufo = defcon.Font(args.ufo)
    ttf = ufo2ft.compileTTF(ufo, useProductionNames=False, convertCubics=False)

    if ufo.kerning:
        ttf["kern"] = legacy_kern_table(ufo)

    ttf.save(args.ttf)

    # merge VTT TSI* tables and maxp data
    vttLib.vtt_merge(args.ufo, args.ttf)


def legacy_kern_table(ufo):
    kerning = flatten_kerning(ufo)
    key_kerning = flatten_kerning(ufo, key_glyphs_only=True)
    logger.info("Adding legacy kerning table to the TTF, "
                "total kerning pairs: {}, "
                "pairs kept after flattening: {}".format(len(kerning),
                                                         len(key_kerning)))

    kern = fontTools.ttLib.newTable("kern")
    kern.version = 0
    subtable = fontTools.ttLib.tables._k_e_r_n.KernTable_format_0()
    subtable.coverage = 1
    subtable.version = 0
    subtable.kernTable = {}
    subtable.kernTable.update(key_kerning)
    kern.kernTables = [subtable]

    return kern

# The flattening algorithm filters out all character by character kerning pairs
# and only leaves in group by group and (group|character) by (character|group)
# pairs. This reduces the number of pairs drastically to better fit in the
# legacy `kern` table.
#
# Reminder from http://unifiedfontobject.org/versions/ufo3/kerning.plist/:
# Kerning groups must begin with standard prefixes. The prefix for groups
# intended for use in the first side of a kerning pair is "public.kern1.". The
# prefix for groups intended for use in the second side of a kerning pair is
# "public.kern2.".
def flatten_kerning(ufo, key_glyphs_only=False):
    kerning = {}
    for (first, second), offset in ufo.kerning.items():
        if offset == 0 and key_glyphs_only:
            continue
        if first.startswith("public.kern") and \
                second.startswith("public.kern"):
            if not key_glyphs_only:
                for first_group in ufo.groups[first]:
                    for second_group in ufo.groups[second]:
                        kerning[(first_group, second_group)] = offset
            else:
                first_group = ufo.groups[first][0]
                second_group = ufo.groups[second][0]
                kerning[(first_group, second_group)] = offset
        elif first.startswith("public.kern"):
            if not key_glyphs_only:
                for first_group in ufo.groups[first]:
                    kerning[(first_group, second)] = offset
            else:
                first_group = ufo.groups[first][0]
                kerning[(first_group, second)] = offset
        elif second.startswith("public.kern"):
            if not key_glyphs_only:
                for second_group in ufo.groups[second]:
                    kerning[(first, second_group)] = offset
            else:
                second_group = ufo.groups[second][0]
                kerning[(first, second_group)] = offset
        # Ubuntu-C has three character x character kerning pairs that aren't
        # picked up by the above flattening algorithm but that are still present
        # in the Google Fonts release. Hack them in here.
        elif first in ("uni023E", "uni0194") or not key_glyphs_only:
            kerning[(first, second)] = offset
    return kerning


if __name__ == "__main__":
    sys.exit(main())
