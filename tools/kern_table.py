import sys
import os
from defcon import Font
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables._k_e_r_n import KernTable_format_0


def flatten_kerning(ufo, key_glyphs_only=False):
    kerning = {}
    for key, value in ufo.kerning.items():
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
        elif not key_glyphs_only:
            kerning[key] = value
    return kerning


def main(args):
    if len(args) < 3:
        sys.exit("usage: kern_table.py ufo ttf output_ttf")
    ufo_path = args[0]
    font_path = args[1]
    output_path = args[2]
    ufo = Font(ufo_path)
    font = TTFont(font_path)

    print("parsing %s to add legacy kern table to %s" % (ufo_path, font_path))

    kerning = flatten_kerning(ufo)
    print("total kerning pairs: %i" % len(kerning))
    key_kerning = flatten_kerning(ufo, key_glyphs_only=True)
    print("kerning pairs kept: %i" % len(key_kerning))

    kern = newTable("kern")
    kern.version = 0

    subtable = KernTable_format_0()
    subtable.coverage = 1
    subtable.version = 0
    subtable.kernTable = {}
    subtable.kernTable.update(key_kerning)
    kern.kernTables = [subtable]
    font["kern"] = kern
    print("writing font with legacy kern table to %s" % output_path)
    font.save(output_path)


if __name__ == "__main__":
    main(sys.argv[1:])
