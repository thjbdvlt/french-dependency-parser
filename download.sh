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
