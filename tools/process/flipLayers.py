# flip background and foreground layers when background exists, maintaining glyph width

import os

basePath = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
sourcesPath = os.path.join(basePath, 'sources')

paths = []
for fileName in os.listdir(sourcesPath):
    if fileName.endswith('.ufo'):
        paths.append(os.path.join(sourcesPath, fileName))

for path in paths:
    f = OpenFont(path, showInterface=False)
    for g in f:
        w = g.width
        if g.getLayer('public.background'):
            g.flipLayers('public.background', 'public.default')
            g.width = w
    f.save()