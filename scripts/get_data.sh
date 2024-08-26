#!/bin/bash

# DOWNLOAD CORPORA
# and other things

# deps:
#   - fd

set -e

root=$(git rev-parse --show-toplevel)
cd "$root"

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

# [ -d corpus/Sequoia ] || git clone ${gh}Sequoia corpus/Sequoia

# delete some useless directories and files
for i in $(fd not-to-release)
do
    rm -rf "$i"
done

# concatenate files and convert into docbin
for i in train dev test
do
    [ -f ${i}.conllu ] || cat $(fd -I ${i}.conllu$) > ${i}.conllu
done

python3 scripts/replace_remove_labels.py

for i in train dev test
do
    rg -v '^\d+-\d' ${i}.conllu | sponge ${i}.conllu
    echo "converting ${i} from .conllu to spacy format..."
    [ -f ${i}.spacy ] || spacy convert ${i}.conllu . -n 10
done

# remove underscore fake-tokens and update attribute head
python3 scripts/remove_underscore.py

# make space-separated docs to avoid tokenization mismatching
python3 scripts/split_tokens.py

# TODO: download vectors from french_word_vectors
# TODO: convert vectors from word2vec to spacy format
