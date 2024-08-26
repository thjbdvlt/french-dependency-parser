#!/bin/bash

# DOWNLOAD CORPORA

# deps:
#   - fd

set -e

# base url
gh=https://github.com/UniversalDependencies/UD_French-

# create directories
[ -d corpus ] || mkdir corpus

# iterate repositories
for i in \
    ParisStories \
    Rhapsodie \
    Sequoia
do
    [ -d corpus/${i} ] || git clone ${gh}${i} corpus/${i}
done

# delete some useless directories and files
for i in $(fd not-to-release)
do
    rm -rf "$i"
done

# concatenate files and convert into docbin
for i in train dev test
do
    [ -f ${i}.conllu ] || cat $(fd -I ${i}.conllu$) > ${i}.conllu
    echo "converting ${i} from .conllu to spacy format..."
    [ -f ${i}.spacy ] || spacy convert ${i}.conllu . -n 10
done

python3 splittokens.py

# download model, unzip, extract
if ! [ -d model ]
then
    wget \
        https://github.com/thjbdvlt/turlututu/releases/download/v0.0.1/model-2024-07-21-00h40.tar.gz \
        -O model.tar.gz
    gunzip model.tar.gz
    tar -xvf model.tar
fi

# delete archive, only keeping the directory model
rm model.tar -rf
