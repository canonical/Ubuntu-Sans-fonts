from fontParts.world import OpenFont
import os

fileNames = [
'Ubuntu-CondensedThin.ufo',
'Ubuntu-CondensedExtraBold.ufo',
'Ubuntu-CondensedExtraBoldItalic.ufo',
'Ubuntu-CondensedLight.ufo',
'Ubuntu-CondensedLightItalic.ufo',
]

basePath = os.path.split(os.path.split(__file__)[0])[0]
sourcesPath = os.path.join(basePath, 'sources')


for fileName in fileNames:
    path = os.path.join(sourcesPath, fileName)
    print('removing kerning from', fileName)
    f = OpenFont(path)
    f.kerning.clear()
    f.kerning[('.notdef', '.notdef')] = 0
    f.save()
    f.close()
    