#!/usr/bin/python
# encoding: utf8

# Smith configuration file for Kanchenjunga

# set the default output folders
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Kanchenjunga'
FAMILY = APPNAME
DESC_SHORT = "Font for the Kirat Rai script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

designspace('source/' + FAMILY + '.designspace',
    target = process('${DS:FILENAME_BASE}.ttf',
       cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo'])),
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/opentype/master.feax", to_ufo = 'True'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
                    metadata=f'../source/{FAMILY}-WOFF-metadata.xml'),
    pdf = fret(params='-oi')
)

