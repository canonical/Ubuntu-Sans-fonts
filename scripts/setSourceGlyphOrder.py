
import os
from fontParts.world import OpenFont

basePath = os.path.split(os.path.split(__file__)[0])[0]
sourcesPath = os.path.join(basePath, 'sources')

lightPath = os.path.join(sourcesPath, 'Ubuntu-Light.ufo')
lightFont = OpenFont(lightPath)
glyphOrder = lightFont.glyphOrder[:]
lightFont.close()

for fileName in os.listdir(sourcesPath):
    filePath = os.path.join(sourcesPath, fileName)
    if filePath.endswith('.ufo'):
        f = OpenFont(filePath)
        # reset font info
        #f.glyphOrder = glyphOrder

print('done')