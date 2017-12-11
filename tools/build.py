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


def flatten_kerning(ufo, key_glyphs_only=False):
    kerning = {}
    for key, value in ufo.kerning.items(): # [(l-hand, r-hand): value, ...]
        if value == 0 and key_glyphs_only:
            continue
        if key[0].startswith("public.kern") and \
                key[1].startswith("public.kern"):
            if not key_glyphs_only:
                for left in ufo.groups[key[0]]:
                    for right in ufo.groups[key[1]]:
                        kerning[(left, right)] = value
            else:
                left = ufo.groups[key[0]][0]
                right = ufo.groups[key[1]][0]
                kerning[(left, right)] = value
        elif key[0].startswith("public.kern"):
            if not key_glyphs_only:
                for left in ufo.groups[key[0]]:
                    kerning[(left, key[1])] = value
            else:
                left = ufo.groups[key[0]][0]
                kerning[(left, key[1])] = value
        elif key[1].startswith("public.kern"):
            if not key_glyphs_only:
                for right in ufo.groups[key[1]]:
                    kerning[(key[0], right)] = value
            else:
                right = ufo.groups[key[1]][0]
                kerning[(key[0], right)] = value
        # Ubuntu-C has three character x character kerning pairs that aren't
        # picked up by the above flattening algorithm but that are still present
        # in the Google Fonts release. Hack them in here.
        elif key[0].startswith("uni023E") or key[0].startswith("uni0194") \
        or not key_glyphs_only:
            kerning[key] = value
    return kerning


if __name__ == "__main__":
    sys.exit(main())
