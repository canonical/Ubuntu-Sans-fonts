import os
from fontTools.ttLib import TTFont

# This script is for fixing incorrect glyphs on the GDEF mark class.
# The offending glyphs are automatically added to the GDEF by fontmake based on the usage of anchors
# We use anchors on them to benefit from automatic positioning while designing the sources.

def getFiles(path, extensions):
    return [os.sep.join((dir, file)) for (dir, dirs, files)
            in os.walk(path) for file in files if
            file.split(".")[-1] in extensions]

legacyMarks = (
    "acute.asc",
    "caron.asc",
    "circumflex.asc",
    "dieresistonos",
    "tonos",
    "uni1FBE",
    "uni1FBE.sc",
    "uni1FBF",
    "uni1FC0",
    "uni1FC1",
    "uni1FCD",
    "acute_greek.sc",
    "grave_greek.sc",
    "double_grave.sc",
    "tonos.sc",
    "uni1FBF.sc",
    "uni1FCD.sc",
    "uni1FCE",
    "uni1FCE.sc",
    "uni1FCF",
    "uni1FCF.sc",
    "uni1FDD",
    "uni1FDD.sc",
    "uni1FDE",
    "uni1FDE.sc",
    "uni1FDF",
    "uni1FDF.sc",
    "uni1FED",
    "uni1FEF",
    "uni1FFD",
    "uni1FFE",
    "uni1FEE",
    "uni1FFE.sc",
)

def fixGDEF(fontPath):
    ttFont = TTFont(fontPath)

    gdef = ttFont["GDEF"].table
    madeChanges = False

    if not hasattr(gdef, "MarkGlyphSetsDef") or not gdef.MarkGlyphSetsDef:
        print("No MarkGlyphSetsDef found in GDEF table.")
    else:
        print("Scanning MarkGlyphSetsDef...")
        for coverage in gdef.MarkGlyphSetsDef.Coverage:
            for i in range(len(coverage.glyphs)-1,-1,-1):
                glyph = coverage.glyphs[i]
                if glyph in legacyMarks:
                    coverage.glyphs.pop(i)
                    print(f"\t Removed {glyph} from GDEF.MarkGlyphSetsDef")
                    madeChanges = True
                elif not (glyph.startswith("uni03") or "comb" in glyph):
                    print(f"\t Possible offending glyph {glyph}")

    if not gdef.GlyphClassDef:
        print("No GlyphClassDef found in GDEF table.")
    else:
        print("Scanning GlyphClassDef...")
        for legacyMark in legacyMarks:
            if legacyMark in gdef.GlyphClassDef.classDefs:
                classType = gdef.GlyphClassDef.classDefs[legacyMark]
                if classType != 1:
                    gdef.GlyphClassDef.classDefs[legacyMark] = 1
                    print(f"\t Switched {legacyMark} from class {classType} to 1")
                    madeChanges = True
    
    if not madeChanges:
        print("No changes")
    else:
        ttFont.save(fontPath, reorderTables=False)
        print("Saved file with modified GDEF table")

    
    
fontsDirPath = ['fonts', 'fonts']
if __name__ == '__main__':
    for dirPath in fontsDirPath:
        fonts = getFiles(dirPath, ['otf', 'ttf'])
        for fontPath in fonts:
            fixGDEF(fontPath)