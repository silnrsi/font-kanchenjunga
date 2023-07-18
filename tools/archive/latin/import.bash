#!/bin/bash

ar=$PWD/tools/archive/latin
glyphnames=$HOME/script/smithplus/etc/glyph_names/glyph_names.csv
import=$HOME/script/latn/font-andika-local/kanchenjunga/Andika

pushd source
for weight in Bold Regular
do
    ufo=Kanchenjunga-${weight}.ufo
    glyphs=$ar/import-${weight}.csv

    # prepare
    psfdeleteglyphs -i $ar/delete-${weight}.txt $ufo
    
    # import
    latin=${import}-${weight}.ufo
    # psfgetglyphnames -i $ar/import-${weight}.txt -a $glyphnames $latin $glyphs
    psfcopyglyphs --rename rename --unicode usv -s $latin -i $glyphs -l tmp.log $ufo
done
for weight in Bold
do
    ufo=Kanchenjunga-${weight}.ufo

    # cleanup
    psfrenameglyphs -i $ar/rename.csv $ufo
    psfsetunicodes -i $ar/encode.csv $ufo
    psfsetmarkcolors -i $ar/import-${weight}.txt -u -c g_light_gray $ufo
done
popd
