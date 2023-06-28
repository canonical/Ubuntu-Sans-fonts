import os
from fontTools.ttLib import TTFont

def getFiles(path, extensions):
    return [os.sep.join((dir, file)) for (dir, dirs, files)
            in os.walk(path) for file in files if
            file.split(".")[-1] in extensions]

def get_name_record(ttFont, nameID, fallbackID=None, platform=(3, 1, 0x409)):
    """Return a name table record which has the specified nameID.
    """
    name = ttFont["name"]
    record = name.getName(nameID, 3, 1, 0x409)
    if not record and fallbackID:
        record = name.getName(fallbackID, 3, 1, 0x409)
    if not record:
        raise ValueError(f"Cannot find record with nameID {nameID}")
    return record.toUnicode()
    
def is_RIBBI(ttFont):
    RIBBI_STYLES = ["Regular", "Italic", "Bold", "Bold Italic"]
    subfamilyName = get_name_record(ttFont, 17)
    return any(token == subfamilyName for token in RIBBI_STYLES)

def fixStaticNames(fontPath):
    WINDOWS_ENGLISH_IDS = 3, 1, 0x409
    ttFont = TTFont(fontPath)
    print (fontPath)

    if "Condensed" in get_name_record(ttFont, 6):
        new_familyName = "Ubuntu Condensed"
        new_subFamilyName = get_name_record(ttFont, 17, 2).replace("Condensed", "").lstrip().rstrip()
        new_subFamilyName = new_subFamilyName if new_subFamilyName != "" else 'Regular'
        new_fullname = new_familyName + " " + new_subFamilyName
        new_postscriptName = new_familyName.replace(' ', '') + "-" + new_subFamilyName.replace(' ', '')
        new_uniqueId = f"{ttFont['head'].fontRevision:.3f}" + ";" + ttFont['OS/2'].achVendID.replace("\x00", " ") + ";" + new_postscriptName
                    
        # Set Typographic Family name
        ttFont['name'].setName(new_familyName, 16, *WINDOWS_ENGLISH_IDS)
        # Set Typographic Style name
        ttFont['name'].setName(new_subFamilyName, 17, *WINDOWS_ENGLISH_IDS)

        # Set Unique font Identifier
        ttFont['name'].setName(new_uniqueId, 3, *WINDOWS_ENGLISH_IDS)

        # Set Full font name
        ttFont['name'].setName(new_fullname, 4, *WINDOWS_ENGLISH_IDS)
        # Set Postscript name
        ttFont['name'].setName(new_postscriptName, 6, *WINDOWS_ENGLISH_IDS)
        
        # Fix names on CFF fonts
        if 'CFF ' in ttFont:
            ttFont['CFF '].cff[0].FamilyName = new_familyName
            ttFont['CFF '].cff.FullName = new_fullname
            ttFont['CFF '].cff.fontNames[0] = new_postscriptName

        if is_RIBBI(ttFont):
            # Remove Typographic Family and Style name for RIBBI fonts
            ttFont['name'].removeNames(16, *WINDOWS_ENGLISH_IDS)
            ttFont['name'].removeNames(17, *WINDOWS_ENGLISH_IDS)

        ttFont.save(fontPath)
            
    
fontsDirPath = ['fonts/otf', 'fonts/ttf']
if __name__ == '__main__':
    for dirPath in fontsDirPath:
        fonts = getFiles(dirPath, ['otf', 'ttf'])
        for fontPath in fonts:
            fixStaticNames(fontPath)