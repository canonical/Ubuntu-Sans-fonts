NORMAL_NAME=Ubuntu
MONO_NAME=UbuntuMono
SRC_DIR=source
CORE_FONTS=B BI R RI
ALL_FONTS=$(CORE_FONTS) C L LI M MI

MASTER_DIR=master_ttf
BUILD_DIR=build

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
	python tools/build.py $< $@

$(BUILD_DIR)/%.ttf: $(SRC_DIR)/%.ttf
	@mkdir -p $(BUILD_DIR)
	python -m vttLib compile --ship $< $@
	tools/update-hinted-metrics.sh $@
	python tools/postprocess-hdmx-zero_out_unif000.py $@

clean:
	@rm -rf $(BUILD_DIR)
	@rm -f $(VTT_TTF) $(VTT_MONO_TTF)

update-requirements:
	@bash tools/update-requirements.sh
