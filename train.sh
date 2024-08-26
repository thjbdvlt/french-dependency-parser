#!/bin/bash

# the command to train the model

spacy train config.cfg \
    --code space_tokenizer.py \
    --output ./model
