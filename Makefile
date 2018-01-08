NORMAL_NAME=Ubuntu
MONO_NAME=UbuntuMono
SRC_DIR=source
CORE_FONTS=B BI R RI
ALL_FONTS=$(CORE_FONTS) C L LI M MI

MASTER_DIR=master_ttf
BUILD_DIR=build
RELEASE_DIR=release
CP=cp -p

TTF=$(ALL_FONTS:%=$(BUILD_DIR)/$(NORMAL_NAME)-%.ttf)
MONO_TTF=$(CORE_FONTS:%=$(BUILD_DIR)/$(MONO_NAME)-%.ttf)

VTT_TTF=$(ALL_FONTS:%=$(SRC_DIR)/$(NORMAL_NAME)-%.ttf)
VTT_MONO_TTF=$(CORE_FONTS:%=$(SRC_DIR)/$(MONO_NAME)-%.ttf)


all: ttf

ttf: $(TTF) $(MONO_TTF)

vtt: $(VTT_TTF) $(VTT_MONO_TTF)

$(SRC_DIR)/%.ttf: $(SRC_DIR)/%.ufo $(SRC_DIR)/%.ufo/*.plist \
                  $(SRC_DIR)/%.ufo/features.fea \
                  $(SRC_DIR)/%.ufo/glyphs*/*.glif \
                  $(SRC_DIR)/%.ufo/glyphs*/contents.plist \
                  $(SRC_DIR)/%.ufo/data/com.github.fonttools.ttx/*.ttx \
                  $(SRC_DIR)/%.ufo/data/com.daltonmaag.vttLib.plist
	export SOURCE_DATE_EPOCH=`python tools/print-mtime.py VERSION.txt`
	python tools/build.py $< $@

$(BUILD_DIR)/%.ttf: $(SRC_DIR)/%.ttf
	@mkdir -p $(BUILD_DIR)
	python -m vttLib compile --ship $< $@
	bash tools/update-hinted-metrics.sh $@
	python tools/postprocess-hdmx-zero_out_unif000.py $@
	python tools/postprocess-kern.py $@

clean:
	@rm -rf $(BUILD_DIR)
	@rm -rf $(RELEASE_DIR)
	@rm -f $(VTT_TTF) $(VTT_MONO_TTF)
	@rm -f old-gf-release

update-requirements:
	@bash tools/update-requirements.sh

update-version: VERSION.txt
	python tools/update-version.py

# Run when VTT compilation fails due to unexpected offsets, etc.
update-vtt: $(VTT_TTF) $(VTT_MONO_TTF)
	python tools/update-vtt.py

release: $(TTF) $(MONO_TTF) LICENCE.txt
	rm -rf $(RELEASE_DIR)
	mkdir $(RELEASE_DIR)
	$(CP) $(BUILD_DIR)/Ubuntu-R.ttf $(RELEASE_DIR)/Ubuntu-Regular.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-RI.ttf $(RELEASE_DIR)/Ubuntu-Italic.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-L.ttf $(RELEASE_DIR)/Ubuntu-Light.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-LI.ttf $(RELEASE_DIR)/Ubuntu-LightItalic.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-M.ttf $(RELEASE_DIR)/Ubuntu-Medium.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-MI.ttf $(RELEASE_DIR)/Ubuntu-MediumItalic.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-B.ttf $(RELEASE_DIR)/Ubuntu-Bold.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-BI.ttf $(RELEASE_DIR)/Ubuntu-BoldItalic.ttf
	$(CP) $(BUILD_DIR)/Ubuntu-C.ttf $(RELEASE_DIR)/UbuntuCondensed-Regular.ttf
	$(CP) $(BUILD_DIR)/UbuntuMono-R.ttf $(RELEASE_DIR)/UbuntuMono-Regular.ttf
	$(CP) $(BUILD_DIR)/UbuntuMono-RI.ttf $(RELEASE_DIR)/UbuntuMono-Italic.ttf
	$(CP) $(BUILD_DIR)/UbuntuMono-B.ttf $(RELEASE_DIR)/UbuntuMono-Bold.ttf
	$(CP) $(BUILD_DIR)/UbuntuMono-BI.ttf $(RELEASE_DIR)/UbuntuMono-BoldItalic.ttf
	$(CP) LICENCE.txt $(RELEASE_DIR)/LICENSE.txt

download-old-gf-release: old-gf-release/Ubuntu-Regular.ttf
old-gf-release/Ubuntu-Regular.ttf:
	sh tools/download-old-gf-release.sh
