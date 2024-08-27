#!/bin/bash

set -e

# check arguments
if [ $# != 2 ]
then
    echo 'missing arg(s)'
    echo "usage: $0 <TAG> <NOTES>"
    exit 1
fi

# remove files
rm -rf model-parser model-parser.tar model-parser.tar.gz

# get the best model
cp -r model/model-best model-parser

# archive (tar) and zip (gzip)
tar cvf model-parser.tar model-parser
gzip model-parser.tar

# check that a file exists
[ -f model-parser.tar.gz ] || {
    echo 'failed creating the release file.'
    exit 1
}

# release
gh release create "$1" model-parser.tar.gz \
    --title "$1" --latest=true --notes "$2"
