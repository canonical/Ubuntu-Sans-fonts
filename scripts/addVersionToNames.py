# Add version number to the name, for easily installation of multiple versions
# addVersionToNames.py /path/to/Font1.otf /path/to/Font2.otf

from fontTools.ttLib import TTFont
import sys
import os

paths = sys.argv[1:]

for path in paths:
    path = path.strip('\"')
    f = TTFont(path)


    findName = f['name'].getName(16, 3, 1, 0x409).toUnicode()
    print('find', findName)
    versionName = f['name'].getName(3, 3, 1, 0x409).toUnicode()
    versionNumber = versionName.split(';')[0]
    varNoSpace = 'Beta'+versionNumber
    varSpace = ' ' + varNoSpace


    for namerecord in f['name'].names:
        nameRecordString = namerecord.toUnicode()
        if findName in nameRecordString:
            newName = nameRecordString.replace(findName, findName+varNoSpace)
            print('Changing name', namerecord.toUnicode(), 'to', newName )
            f['name'].setName(newName, namerecord.nameID, namerecord.platformID, namerecord.platEncID, namerecord.langID)
            
    
    #os.remove(path)
    basePath, fileName = os.path.split(path)
    newFilename = fileName.replace(findName, findName+varNoSpace)
    
    newPath = os.path.join(basePath, newFilename)
    f.save(newPath)