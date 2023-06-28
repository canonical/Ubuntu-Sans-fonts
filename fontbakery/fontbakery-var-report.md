## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[12] Ubuntu-Italic[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.869" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd. Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Normal | wdth | 100.0 | 2 | None | 100.0 | 2 | None |
| Condensed | wdth | 75.0 | 0 | None | 75.0 | 0 | None |
| SemiCondensed | wdth | N/A | N/A | N/A | 87.5 | 0 | None |
| Thin | wght | 100.0 | 0 | None | 100.0 | 0 | None |
| ExtraLight | wght | N/A | N/A | N/A | 200.0 | 0 | None |
| Light | wght | 300.0 | 0 | None | 300.0 | 0 | None |
| Regular | wght | 400.0 | 2 | 700.0 | 400.0 | 2 | 700.0 |
| Medium | wght | 500.0 | 0 | None | 500.0 | 0 | None |
| SemiBold | wght | N/A | N/A | N/A | 600.0 | 0 | None |
| Bold | wght | 700.0 | 0 | None | 700.0 | 0 | None |
| ExtraBold | wght | 800.0 | 0 | None | 800.0 | 0 | None |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Add missing instances
- Delete additional instances

| Name | current | expected |
| :--- | :--- | :--- |
| Condensed Light Italic | wdth=75.0, wght=300.0 | N/A |
| Condensed Italic | wdth=75.0, wght=400.0 | N/A |
| Condensed ExtraBold Italic | wdth=75.0, wght=800.0 | N/A |
| Condensed Thin Italic | wdth=75.0, wght=100.0 | N/A |
| Condensed Medium Italic | wdth=75.0, wght=500.0 | N/A |
| Condensed Bold Italic | wdth=75.0, wght=700.0 | N/A |
| Thin Italic | wdth=100.0, wght=100.0 | wdth=100.0, wght=100.0 |
| ExtraLight Italic | N/A | wdth=100.0, wght=200.0 |
| Light Italic | wdth=100.0, wght=300.0 | wdth=100.0, wght=300.0 |
| Italic | wdth=100.0, wght=400.0 | wdth=100.0, wght=400.0 |
| Medium Italic | wdth=100.0, wght=500.0 | wdth=100.0, wght=500.0 |
| SemiBold Italic | N/A | wdth=100.0, wght=600.0 |
| Bold Italic | wdth=100.0, wght=700.0 | wdth=100.0, wght=700.0 |
| ExtraBold Italic | wdth=100.0, wght=800.0 | wdth=100.0, wght=800.0 | [code: bad-fvar-instances]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha
	* Alphatonos and 959 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- NULL

	- ampersand.001

	- eight_fraction_nine

	- five_fraction_nine

	- five_fraction_seven

	- four_fraction_nine

	- four_fraction_seven

	- ijacute

	- seven_fraction_nine 

	- 5 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 1 start point differs in glyph 'zero' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0>

	- Contour 1 start point differs in glyph 'o' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0>

	- Contour 1 start point differs in glyph 'ohorn' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0>

	- Contour 1 start point differs in glyph 'uni01A3' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0>

	- Contour 1 start point differs in glyph 'uni01EB' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0>

	- Contour 1 start point differs in glyph 'yucy' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d44df0> 

	- Contour order differs in glyph 'ijacute': [0, 1, 2, 3] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119c74cd0>, [0, 1, 3, 2] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x119d459c0>. [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute.asc (unencoded), caron.asc (unencoded), circumflex.asc (unencoded), dieresis_acute (unencoded), dieresis_acute.cap (unencoded), dieresis_breve (unencoded), dieresis_breve.cap (unencoded), dieresis_grave (unencoded), dieresis_grave.cap (unencoded), dieresis_macron (unencoded) and 19 more.

Use -F or --full-lists to disable shortening of long lists. [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0384, U+0385, U+1FBE, U+1FBF, U+1FC0, U+1FC1, U+1FCD, U+1FCE, U+1FCF, U+1FDD and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: non-mark-chars]
</div></details><br></div></details><details><summary><b>[12] Ubuntu[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.869" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd. Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Normal | wdth | 100.0 | 2 | None | 100.0 | 2 | None |
| Condensed | wdth | 75.0 | 0 | None | 75.0 | 0 | None |
| SemiCondensed | wdth | N/A | N/A | N/A | 87.5 | 0 | None |
| Thin | wght | 100.0 | 0 | None | 100.0 | 0 | None |
| ExtraLight | wght | N/A | N/A | N/A | 200.0 | 0 | None |
| Light | wght | 300.0 | 0 | None | 300.0 | 0 | None |
| Regular | wght | 400.0 | 2 | 700.0 | 400.0 | 2 | 700.0 |
| Medium | wght | 500.0 | 0 | None | 500.0 | 0 | None |
| SemiBold | wght | N/A | N/A | N/A | 600.0 | 0 | None |
| Bold | wght | 700.0 | 0 | None | 700.0 | 0 | None |
| ExtraBold | wght | 800.0 | 0 | None | 800.0 | 0 | None |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Add missing instances
- Delete additional instances

| Name | current | expected |
| :--- | :--- | :--- |
| Condensed Thin | wdth=75.0, wght=100.0 | N/A |
| Condensed ExtraBold | wdth=75.0, wght=800.0 | N/A |
| Condensed Light | wdth=75.0, wght=300.0 | N/A |
| Condensed Regular | wdth=75.0, wght=400.0 | N/A |
| Condensed Medium | wdth=75.0, wght=500.0 | N/A |
| Condensed Bold | wdth=75.0, wght=700.0 | N/A |
| Thin | wdth=100.0, wght=100.0 | wdth=100.0, wght=100.0 |
| ExtraLight | N/A | wdth=100.0, wght=200.0 |
| Light | wdth=100.0, wght=300.0 | wdth=100.0, wght=300.0 |
| Regular | wdth=100.0, wght=400.0 | wdth=100.0, wght=400.0 |
| Medium | wdth=100.0, wght=500.0 | wdth=100.0, wght=500.0 |
| SemiBold | N/A | wdth=100.0, wght=600.0 |
| Bold | wdth=100.0, wght=700.0 | wdth=100.0, wght=700.0 |
| ExtraBold | wdth=100.0, wght=800.0 | wdth=100.0, wght=800.0 | [code: bad-fvar-instances]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 1.0Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha
	* Alphatonos and 959 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- eight_fraction_nine

	- five_fraction_nine

	- five_fraction_seven

	- four_fraction_nine

	- four_fraction_seven

	- ijacute

	- seven_fraction_nine

	- six_fraction_seven

	- three_fraction_seven

	- two_fraction_nine 

	- two_fraction_seven
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute_greek.sc (unencoded), dieresistonos (U+0385), grave_greek.sc (unencoded), tonos (U+0384), tonos.sc (unencoded), uni1FBE (U+1FBE), uni1FBF (U+1FBF), uni1FBF.sc (unencoded), uni1FC0 (U+1FC0), uni1FC1 (U+1FC1) and 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0384, U+0385, U+1FBE, U+1FBF, U+1FC0, U+1FC1, U+1FCD, U+1FCE, U+1FCF, U+1FDD and 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: non-mark-chars]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 16 | 196 | 17 | 238 | 0 |
| 0% | 2% | 3% | 41% | 4% | 50% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
