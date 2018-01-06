#!/bin/env python3
#
# Prints the modification time of a file in a cross-platform way. Used to set
# the SOURCE_DATE_EPOCH environment variable to get more deterministic builds.


import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="File to print mtime of.")
args = parser.parse_args()

print(int(os.path.getmtime(args.file)))
