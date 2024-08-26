de quoi s'agit-il?
d'un _parser_, d'un _syntactic dependencies parser_.
un modèle que je vais entraîner avec spacy en utilisant mes vectors.
pour pouvoir l'utiliser avec le reste de mon modèle.

ne PAS entraîner les morphologies, parce que par exemple pas de `Number[psor]` pour "ses", "leur", etc., donc moins d'informations sur les pronoms que les données que j'ai entraînées.
