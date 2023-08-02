# Ubuntu Font Family

[![][Fontbakery]](https://canonical.github.io/Ubuntu-fonts/fontbakery/fontbakery-report.html)
[![][Universal]](https://canonical.github.io/Ubuntu-fonts/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://canonical.github.io/Ubuntu-fonts/fontbakery/fontbakery-report.html)
[![][Outline Correctness]](https://canonical.github.io/Ubuntu-fonts/fontbakery/fontbakery-report.html)
[![][Shaping]](https://canonical.github.io/Ubuntu-fonts/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcanonical%2FUbuntu-fonts%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcanonical%2FUbuntu-fonts%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcanonical%2FUbuntu-fonts%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcanonical%2FUbuntu-fonts%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcanonical%2FUbuntu-fonts%2Fgh-pages%2Fbadges%2FUniversal.json

The **Ubuntu Font Family** are a set of matching libre/open fonts. The fonts were originally developed in 2010–2011, further expanded and improved in 2015, and expanded again in 2022–2023 when variable fonts were added. 

The development is being funded by Canonical Ltd on behalf the wider Free Software community and the Ubuntu project. The technical font design work and implementation has been undertaken by [Dalton Maag](http://daltonmaag.com), [Type Network](http://typenetwork.com), [DJR](http://djr.com), and [Dual Type](http://dualtype.design).

Both the final font TrueType/OpenType files and the design files used to produce the font family are distributed under an open licence and you are expressly encouraged to experiment, modify, share and improve.

[http://font.ubuntu.com/](http://font.ubuntu.com/)

A monospaced/fixed-width variant, **Ubuntu Mono**, is available in a separate repository: [https://github.com/canonical/ubuntumono-fonts](https://github.com/canonical/ubuntumono-fonts)

![Sample Image](documentation/image1.png)

## Releases

You can find recent releases and release candidates in the ["Releases" tab](https://github.com/canonical/Ubuntu-fonts/releases).

## Building

Fonts are built automatically by GitHub Actions - take a look in the ["Actions" tab](https://github.com/canonical/Ubuntu-fonts/actions) for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make dev` will produce only variable font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://canonical.github.io/Ubuntu-fonts.

It is possible to generate custom styles directly from the variable fonts using [fontTools instancer.](https://fonttools.readthedocs.io/en/latest/varLib/instancer.html). For example, the following generates a custom style that is a close match to Ubuntu Mono’s original weight:

```fonttools varLib.instancer Ubuntu[wdth,wght].ttf wdth=100 wght=473```


## Changelog

See [FONTLOG.txt](FONTLOG.txt) for a summary of updates.

## License

This Font Software is licensed under the UBUNTU FONT LICENCE Version 1.0
This license is available with a FAQ at
https://ubuntu.com/legal/font-licence

