#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
# DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Kanchenjunga'
FAMILY = APPNAME
DESC_SHORT = "Font for the Kirat Rai script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

designspace('source/' + FAMILY + '.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
#    opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/features.feax", to_ufo = 'True'),
#    woff = woff('web/${DS:FILENAME_BASE}.woff',
#        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
#        cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
#        ),
    pdf = fret(params='-oi')
)
