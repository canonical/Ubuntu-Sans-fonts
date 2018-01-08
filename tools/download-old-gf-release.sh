#!/bin/env sh

export GF="https://github.com/google/fonts/raw/a50de97857f6626d6628c91e6a34c12ee8a16ede/ufl"

mkdir -p old-gf-release
cd old-gf-release

wget ${GF}/ubuntu/Ubuntu-Bold.ttf
wget ${GF}/ubuntu/Ubuntu-BoldItalic.ttf
wget ${GF}/ubuntu/Ubuntu-Italic.ttf
wget ${GF}/ubuntu/Ubuntu-Light.ttf
wget ${GF}/ubuntu/Ubuntu-LightItalic.ttf
wget ${GF}/ubuntu/Ubuntu-Medium.ttf
wget ${GF}/ubuntu/Ubuntu-MediumItalic.ttf
wget ${GF}/ubuntu/Ubuntu-Regular.ttf

wget ${GF}/ubuntumono/UbuntuMono-Bold.ttf
wget ${GF}/ubuntumono/UbuntuMono-BoldItalic.ttf
wget ${GF}/ubuntumono/UbuntuMono-Italic.ttf
wget ${GF}/ubuntumono/UbuntuMono-Regular.ttf

wget ${GF}/ubuntucondensed/UbuntuCondensed-Regular.ttf
