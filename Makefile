NORMAL_NAME=Ubuntu
MONO_NAME=UbuntuMono
SRCDIR=source
CORE_FONTS=B BI R RI
ALL_FONTS=$(CORE_FONTS) C L LI M MI
TTF=$(ALL_FONTS:%=$(BUILD_DIR)/$(NORMAL_NAME)-%.ttf)
MONO_TTF=$(CORE_FONTS:%=$(BUILD_DIR)/$(MONO_NAME)-%.ttf)
MASTER_DIR=master_ttf
BUILD_DIR=build

all: ttf

ttf: $(TTF) $(MONO_TTF)

$(BUILD_DIR)/%.ttf: $(SRCDIR)/%.ufo
	fontmake --keep-overlaps --no-production-names --keep-direction -o ttf -u $<
	@mkdir -p $(BUILD_DIR)
	FILE=$$(ls $(MASTER_DIR)); \
	mv $(MASTER_DIR)/$$FILE $@;

clean:
	@rm -rf $(BUILD_DIR) $(MASTER_DIR)
