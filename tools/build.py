import sys
import logging
import defcon
import ufo2ft
import vttLib
import argparse


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("ufo", type=str, help="The path to the input UFO.")
    parser.add_argument("ttf", type=str, help="The path to the output TTF.")
    args = parser.parse_args()

    logging.basicConfig(level="INFO")

    ufo = defcon.Font(args.ufo)
    ttf = ufo2ft.compileTTF(ufo, useProductionNames=False, convertCubics=False)
    ttf.save(args.ttf)

    # merge VTT TSI* tables and maxp data
    vttLib.vtt_merge(args.ufo, args.ttf)

if __name__ == "__main__":
    sys.exit(main())
