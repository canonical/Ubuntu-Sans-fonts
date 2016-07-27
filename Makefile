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
                  $(SRC_DIR)/%.ufo/data/com.github.fonttools.ttx/*.ttx
	fontmake --keep-overlaps --no-production-names --keep-direction -o ttf -u $<
	@FILE=$$(ls $(MASTER_DIR)); \
	mv $(MASTER_DIR)/$$FILE $@;
	@rm -r $(MASTER_DIR)
	python -m vttLib merge $< $@

$(BUILD_DIR)/%.ttf: $(SRC_DIR)/%.ttf
	@mkdir -p $(BUILD_DIR)
	python -m vttLib compile --ship $< $@

clean:
	@rm -rf $(BUILD_DIR)
	@rm -f $(VTT_TTF) $(VTT_MONO_TTF)
