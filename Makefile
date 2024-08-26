train.spacy:
	./scripts/get_data.sh

train: train.spacy
	spacy train config.cfg \
		--code space_tokenizer.py \
		--output ./model

clean:
	rm -rf *.conllu *.spacy
