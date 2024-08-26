#!/bin/bash

# DOWNLOAD CORPORA

# deps:
#   - fd

set -e

# base url
gh=https://github.com/UniversalDependencies/UD_French-

# create directory
[ -d corpus ] || mkdir corpus

# iterate repositories
for i in \
    ParisStories \
    Rhapsodie \
    Sequoia
do
    git clone ${gh}${i} corpus/${i}
done

# delete some useless directories and files
for i in $(fd not-to-release)
do
    rm -rf "$i"
done

# concatenate files
for i in train dev test
do
    cat $(fd -I ${i}.conllu$) > ${i}.conllu
done

# download model, unzip, extract
wget \
    https://github.com/thjbdvlt/turlututu/releases/download/v0.0.1/model-2024-07-21-00h40.tar.gz \
    -O model.tar.gz
gunzip model.tar.gz
tar -xvf model.tar

# delete archive, only keeping the directory model
rm model.tar -rf
