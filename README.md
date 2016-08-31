# Ubuntu Font Family

The Ubuntu Font Family are a set of matching new libre/open fonts in
development during 2010--2011.  And with further expansion work and
bug fixing during 2015.  The development is being funded by
Canonical Ltd on behalf the wider Free Software community and the
Ubuntu project.  The technical font design work and implementation is
being undertaken by Dalton Maag.

Both the final font Truetype/OpenType files and the design files used
to produce the font family are distributed under an open licence and
you are expressly encouraged to experiment, modify, share and improve.

  http://font.ubuntu.com/

--------------------
# Build instructions

It is recommended to use a virtual environment with `pyenv`, since we use
specific versions of some dependencies that might be differ from those installed
system wide.

Install dependencies
```sh
$ pip install -r requirements.txt
```

Build fonts
```
$ make
```

-----------------------------
# Add hdmx, LTSH, VDMX tables

Download CacheTT (from [Microsoft Font Tools](https://www.microsoft.com/en-us/Typography/tools.aspx))

```sh
$ curl -o FontTools.exe http://download.microsoft.com/download/f/f/a/ffae9ec6-3bf6-488a-843d-b96d552fd815/FontTools.exe
```

Unzip FontTools.exe and FontTools/CacheTT.zip


Add hdmx, LTSH, VDMX table to font on Linux or OS X:
```sh
$ wine CacheTT/cachett.exe INPUT_FILE OUTPUT_FILE
```

... or on Windows:
```
$ CacheTT/cachett.exe INPUT_FILE OUTPUT_FILE
```

-----------------------------
# Miscellaneous

- [kern-dump](https://github.com/adobe-type-tools/kern-dump):
  tool to dump the kerning. This can be used to diff kerning between two fonts.
- [fontdiff](https://github.com/googlei18n/fontdiff):
  tool to compare two rendered fonts visually.

-----------------------------
# Roadmap:
- [x] convert sources to UFO
- [x] generate TTF from UFO
- [x] store VTT sources in UFO
- [x] translate VTT assembly to fontTools TTInstructions
- [ ] generate kern table
