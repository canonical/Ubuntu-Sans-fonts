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

Download Microsoft CacheTT
```sh
$ curl -o FontTools.exe http://download.microsoft.com/download/f/f/a/ffae9ec6-3bf6-488a-843d-b96d552fd815/FontTools.exe
```

Unpack with unzip
```sh
$ unzip FontTools.exe
$ unzip FontTools/CacheTT.zip
```

Add hdmx, LTSH, VDMX table to font
```sh
$ wine FontTools/CacheTT/cachett.exe FONT_FILE
```
