#!/usr/bin/env python3
#
# In the Google Fonts release, the GPOS and legacy kern table disagree on
# various kernings, especially in C. We treat the GPOS table as the canonical
# one (it's what modern layout libraries use) and simply patch the legacy kern
# table in the generated binaries.


import os
import sys
import argparse
import fontTools.ttLib

parser = argparse.ArgumentParser()
parser.add_argument("ttf", type=str, help="The path to the input TTF.")
args = parser.parse_args()

ttf = fontTools.ttLib.TTFont(args.ttf)

if not "kern" in ttf:
    sys.exit(0)

kt = ttf["kern"].kernTables[0].kernTable

if "Ubuntu-M.ttf" in args.ttf:
    del kt[('Gamma', 'uni1F76')]
    del kt[('Gamma', 'uni1F77')]
    del kt[('Tau', 'uni1F77')]
    del kt[('Psi', 'uni1F35')]
elif "Ubuntu-MI.ttf" in args.ttf:
    kt[('Gamma', 'uni1F76')] = -12
    kt[('Gamma', 'uni1F77')] = -17
    del kt[('Tau', 'uni1F76')]
    kt[('Tau', 'uni1F77')] = -25
    del kt[('Tau', 'uni1FD0')]
    del kt[('Chi', 'uni1FD1')]
elif "Ubuntu-L.ttf" in args.ttf:
    del kt[('Upsilon', 'uni1F34')]
elif "Ubuntu-LI.ttf" in args.ttf:
    del kt[('Kappa', 'uni1FD6')]
    del kt[('Tau', 'uni1F76')]
    kt[('Upsilon', 'uni1F34')] = 52
elif "Ubuntu-C.ttf" in args.ttf:
    del kt[('uni01B3', 'ampersand')]
    del kt[('uni01B3', 'quotesingle')]
    del kt[('uni01B3', 'parenleft')]
    del kt[('uni01B3', 'parenright')]
    del kt[('uni01B3', 'asterisk')]
    del kt[('uni01B3', 'hyphen')]
    del kt[('uni01B3', 'period')]
    del kt[('uni01B3', 'slash')]
    del kt[('uni01B3', 'colon')]
    del kt[('uni01B3', 'question')]
    del kt[('uni01B3', 'at')]
    del kt[('uni01B3', 'A')]
    del kt[('uni01B3', 'C')]
    del kt[('uni01B3', 'G')]
    del kt[('uni01B3', 'J')]
    del kt[('uni01B3', 'M')]
    del kt[('uni01B3', 'O')]
    del kt[('uni01B3', 'Q')]
    del kt[('uni01B3', 'T')]
    kt[('uni01B3', 'V')] = 40
    del kt[('uni01B3', 'W')]
    del kt[('uni01B3', 'X')]
    del kt[('uni01B3', 'Y')]
    del kt[('uni01B3', 'Z')]
    del kt[('uni01B3', 'backslash')]
    del kt[('uni01B3', 'bracketright')]
    kt[('uni01B3', 'a')] = -84
    kt[('uni01B3', 'c')] = -95
    kt[('uni01B3', 'd')] = -95
    kt[('uni01B3', 'e')] = -95
    kt[('uni01B3', 'g')] = -95
    kt[('uni01B3', 'n')] = -80
    kt[('uni01B3', 'o')] = -95
    kt[('uni01B3', 'p')] = -80
    kt[('uni01B3', 'q')] = -95
    kt[('uni01B3', 'r')] = -80
    kt[('uni01B3', 's')] = -80
    kt[('uni01B3', 'u')] = -76
    kt[('uni01B3', 'v')] = -48
    kt[('uni01B3', 'w')] = -40
    kt[('uni01B3', 'x')] = -40
    kt[('uni01B3', 'y')] = -48
    kt[('uni01B3', 'z')] = -53
    del kt[('uni01B3', 'braceleft')]
    del kt[('uni01B3', 'braceright')]
    del kt[('uni01B3', 'guilsinglleft')]
    del kt[('uni01B3', 'quoteleft')]
    del kt[('uni01B3', 'quoteright')]
    del kt[('uni01B3', 'guilsinglright')]
    del kt[('uni01B3', 'AE')]
    del kt[('uni01B3', 'adieresis')]
    del kt[('uni01B3', 'edieresis')]
    del kt[('uni01B3', 'igrave')]
    del kt[('uni01B3', 'iacute')]
    del kt[('uni01B3', 'icircumflex')]
    del kt[('uni01B3', 'idieresis')]
    kt[('uni01B3', 'eth')] = -95
    kt[('uni01B3', 'thorn')] = -80
    kt[('uni01B3', 'itilde')] = 50
    kt[('uni01B3', 'imacron')] = 40
    kt[('uni01B3', 'ibreve')] = 30
    del kt[('uni01B3', 'napostrophe.case')]
    kt[('uni01B3', 'eng')] = -80
    del kt[('uni01B3', 'Parenleft')]
    del kt[('uni01B3', 'Parenright')]
    del kt[('uni01B3', 'Hyphen')]
    del kt[('uni01B3', 'Slash')]
    del kt[('uni01B3', 'At')]
    del kt[('uni01B3', 'Backslash')]
    del kt[('uni01B3', 'Bracketright')]
    del kt[('uni01B3', 'Braceleft')]
    del kt[('uni01B3', 'Braceright')]
    del kt[('uni01B3', 'Guilsinglleft')]
    del kt[('uni01B3', 'Guilsinglright')]
    kt[('uni01B3', 'uni0181')] = 44
    kt[('uni01B3', 'uni018D')] = -95
    del kt[('uni01B3', 'uni0190')]
    kt[('uni01B3', 'uni019B')] = 29
    del kt[('uni01B3', 'uni019C')]
    kt[('uni01B3', 'uni01AA')] = 134
    kt[('uni01B3', 'uni01B7')] = 34
    kt[('uni01B3', 'uni01B8')] = 19
    kt[('uni01B3', 'uni01BA')] = -23
    kt[('uni01B3', 'uni01BB')] = 13
    kt[('uni01B3', 'uni01BC')] = 45
    kt[('uni01B3', 'uni01BE')] = 20
    kt[('uni01B3', 'uni01BF')] = -80
    del kt[('uni01B3', 'uni01DD')]
    kt[('uni01B3', 'uni01DF')] = -24
    del kt[('uni01B3', 'uni01F0')]
    kt[('uni01B3', 'uni0201')] = -14
    kt[('uni01B3', 'uni0205')] = -45
    kt[('uni01B3', 'uni020B')] = 40
    del kt[('uni01B3', 'uni0211')]
    kt[('uni01B3', 'uni021C')] = 46
    kt[('uni01B3', 'uni021D')] = -34
    del kt[('uni01B3', 'uni0234')]
elif "Ubuntu-B.ttf" in args.ttf:
    del kt[('Gamma', 'uni1F35')]
    del kt[('Gamma', 'uni1FD1')]
    del kt[('Kappa', 'uni1FD0')]
    del kt[('Psi', 'uni1F34')]
elif "Ubuntu-BI.ttf" in args.ttf:
    kt[('Gamma', 'uni1F35')] = 1
    kt[('Gamma', 'uni1FD1')] = 10
    del kt[('Gamma', 'uni1FD6')]
    del kt[('Kappa', 'uni1F34')]
    kt[('Kappa', 'uni1FD0')] = -10
    del kt[('Upsilon', 'uni1F76')]

ttf.save(args.ttf)
