__syntactic dependency parser__ for french with [spacy](https://spacy.io/api/).

this repository is comprised of scripts that fetch and prepare data to train a [syntactic dependencies](https://universaldependencies.org/u/dep/) parser with [spacy](https://spacy.io/api/) for the french language, along with a configuration file and script to train it. the __model__ itself is available under __releases__.

the data used for the training is an aggregation of three [UD](https://universaldependencies.org/) datasets and makes some minor changes to these datasets.

in the datasets i used, the word _du_ is splitted into its logical component _de_ and _le_. a text like _on parle du ciel_ becomes _on parle de le ciel_ in the `.conllu` files. but in the texts i have to analyze, _du_ isn't splitted at all, so i need to unsplit it. thus the following:

```conllu
11-12	du	...	_	_	_	_
11	de	...	19	case	_	_
12	le	...	11	det	_	_
```

is transformed into:

```conllu
11	du	...	19	case:det	_	_
```

upon that, some labels are replaced by others, and sentences containing certain labels (such as `dep` which indicates than the parsing failed) are removed. for a list of replaced or removed labels, refer the file [labels_lookup.txt](./labels_lookup.txt).

usage
-----

the __parser__ is not a full pipeline. you have to source it from another pipeline as a component:

```python3
import spacy

# load your main pipeline
nlp = spacy.load('fr_core_news_sm', exclude=['parser'])

# load the model containing the parser
nlp_deps = spacy.load('./model', exclude=['tokenizer'])

# put the parser in the main pipeline
nlp.add_pipe('parser', source=nlp_deps)
```
