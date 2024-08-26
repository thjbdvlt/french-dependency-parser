*__[syntactic dependencies](https://universaldependencies.org/u/dep/) [parser](https://spacy.io/api/dependencyparser)__* for french with [spacy](https://spacy.io/api/).

this repository is comprised of scripts that fetch and prepare data to train a __dependency parser__ with [spacy](https://spacy.io/api/) for the french language, along with a configuration file and script to train it. the __model__ itself is available under __releases__.

the data used for the training is an aggregation of three [UD](https://universaldependencies.org/) datasets and makes some minor changes to these datasets.


the following:

```conllu
11-12	du	_	_	_	_	_	_	_	_
11	de	de	ADP	_	...	19	case	_	_
12	le	le	DET	_	...	11	det	_	_
```

is transformed into:

```conllu
11	de	de	ADP	_	...	19	case:det	_	_
```

some labels are replaced by others, and sentences containing certain labels (such as `dep` which indicates than the parsing failed) are removed. for a list of replaced or removed labels, refer the file [lookup.txt](./lookup.txt).
