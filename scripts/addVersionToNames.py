# Add version number to the name, for easily installation of multiple versions
# addVersionToNames.py /path/to/Font1.otf /path/to/Font2.otf

from fontTools.ttLib import TTFont
import sys
import os

paths = sys.argv[1:]


def get_name_record(ttFont, nameID, fallbackID=None, platform=(3, 1, 0x409)):
    name = ttFont["name"]
    record = name.getName(nameID, 3, 1, 0x409)
    if not record and fallbackID:
        record = name.getName(fallbackID, 3, 1, 0x409)
    if not record:
        raise ValueError(f"Cannot find record with nameID {nameID}")
    return record.toUnicode()

for path in paths:
    path = path.strip('\"')
    f = TTFont(path)


    findName = get_name_record(f, 16, fallbackID=1)
    print('find', findName)
    versionName = get_name_record(f, 3, fallbackID=1)
    versionNumber = versionName.split(';')[0]
    varNoSpace = 'Beta'+versionNumber
    varSpace = ' ' + varNoSpace


    for namerecord in f['name'].names:
        nameRecordString = namerecord.toUnicode()
        if findName in nameRecordString:
            newName = nameRecordString.replace(findName, findName+varNoSpace)
            print(f'Changing name record {namerecord.nameID}: {namerecord.toUnicode()} to {newName}')
            f['name'].setName(newName, namerecord.nameID, namerecord.platformID, namerecord.platEncID, namerecord.langID)
            
    
    #os.remove(path)
    basePath, fileName = os.path.split(path)
    newFilename = fileName.replace(findName, findName+varNoSpace)
    
    newPath = os.path.join(basePath, newFilename)
    f.save(newPath)