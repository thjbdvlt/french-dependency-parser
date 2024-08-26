#!/bin/bash

rg '\t[^\t_]+\t_\t_$' --no-ignore -o $(git rev-parse --show-toplevel)/*.conllu | \
    rg -o '\t[^\t_]+' | \
    sort | uniq -c | sort -n
