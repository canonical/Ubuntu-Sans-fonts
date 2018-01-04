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

# Build instructions

It is recommended to use a virtual environment with `python -m virtualenv`,
since we use specific versions of some dependencies that might be differ
from those installed system wide.

Install dependencies
```sh
$ pip install -r requirements.txt
# Also install wine and curl.
```

Build fonts
```
$ make
```

Build fonts to edit TrueType instructions in VTT (placed next to the UFO)
```
$ make vtt
```

When making changes to the source files, the VTT compilation step may fail due
to "unexpected" errors. The sources contain VTT source in high-level and
compiled forms, vttLib checks that various things in the source line up with
what's written to the VTT data and will complain if there are mismatches. Run
the following to update the VTT data within the source:
```
$ make update-vtt
```

# Miscellaneous

- [fonttools](https://github.com/fonttools/fonttools): Includes the tool `ttx`
  that can be used to dump the contens of font binaries in XML form for easier
  comparison.
- [kern-dump](https://github.com/adobe-type-tools/kern-dump): Tool to dump the
  kerning. This can be used to diff kerning between two fonts.
- [fontdiff](https://github.com/googlei18n/fontdiff): Tool to compare two
  rendered fonts visually.

# Roadmap:
- [ ] Match the binaries released on Google Fonts as closely as possible, as
  that version has received the most exposure and patching.
- [ ] Swap the Google Fonts binaries with ones generated from this source and
  fix any issues that come up.
- [ ] Experiment with shipping more internally consistent binaries.
- [ ] Declare a stable version and ship it in Ubuntu
- [ ] Integrate thin weight, Arabic and Hebrew that was done but never released.
- [ ] Plan the future of the typeface. Variable font, how?
