import os

repoPath = os.path.split(os.path.split(__file__)[0])[0]

srcBase = os.path.join(repoPath, "_temp/220512 Ubuntu Binaries from Google Repo")
destBase = os.path.join(repoPath, "fonts/ttf")

fonts = []
fontsBefore = []

for fileName in os.listdir(destBase):
    if fileName.endswith('.ttf'):
        baseFileName = os.path.splitext(fileName)[0]
        srcPath = os.path.join(srcBase, fileName)
        destPath = os.path.join(destBase, fileName)
        outPath = os.path.join(repoPath, 'out')
        fonts.append('"'+destPath+'"')
        fontsBefore.append('"'+srcPath+'"')

fontsAsString = ' '.join(fonts)
fontsBeforeAsString = ' '.join(fontsBefore)
command = f'gftools qa -f "{fontsAsString}" -fb "{fontsBeforeAsString}" -o ../out-diffenator --diffenator'
print(command)
os.system(command)