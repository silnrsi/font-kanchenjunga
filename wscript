#!/usr/bin/python
# encoding: utf8

# Smith configuration file for Kanchenjunga

# set the default output folders
DOCDIR = ["documentation", "web"]
genout = "generated/"

# set the font name and description
APPNAME = 'Kanchenjunga'
FAMILY = APPNAME
DESC_SHORT = "Font for the Kirat Rai script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
omitaps = '--omitaps "L,O,R"'

designspace('source/Kanchenjunga.designspace',
    instanceparams='-l ' + genout + '${DS:FILENAME_BASE}_createinstances.log',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    ),
    version=VERSION,  # Needed to ensure dev information on version string
    ap = genout + '${DS:FILENAME_BASE}.xml',
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", 
        mapfile = genout + "${DS:FILENAME_BASE}.map",
        master="source/opentype/master.feax", to_ufo = 'True'),
    typetuner = typetuner("source/typetuner/feat_all.xml"),
    script='krai',
    pdf = fret(params='-oi'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        ),
    )
