get:
	./get_data.sh

train: train.spacy
	./train.sh

train.spacy: get

clean:
	rm *.conllu *.spacy -rf
