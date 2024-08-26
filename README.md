de quoi s'agit-il?
d'un _parser_, d'un _syntactic dependencies parser_.
un modèle que je vais entraîner avec spacy en utilisant mes vectors.
pour pouvoir l'utiliser avec le reste de mon modèle.

ne PAS entraîner les morphologies, parce que par exemple pas de `Number[psor]` pour "ses", "leur", etc., donc moins d'informations sur les pronoms que les données que j'ai entraînées.

il faut que je modifie un peu les corpus.
parce que surtout il y a ça:

```conllu
11-12	du	_	_	_	_	_	_	_	_
11	de	de	ADP	_	ExtPos=ADV	19	discourse	_	Idiom=Yes
12	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	11	fixed	_	InIdiom=Yes
```

or, les textes ne se présentent pas sous cette forme...
