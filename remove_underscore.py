import spacy
import tqdm
import space_tokenizer

print('removing "_" tokens.')

print("load model...")
nlp = spacy.blank("fr")
nlp.tokenizer = space_tokenizer.BlankTokenizer(nlp.vocab)

for dataset in ("train", "dev", "test"):
    fp = dataset + ".spacy"
    print("current:", fp)
    db = spacy.tokens.DocBin()
    db_new = spacy.tokens.DocBin()
    db.from_disk(fp)
    for doc in tqdm.tqdm(db.get_docs(nlp.vocab)):
        n_underscore = 0
        x = [i for i in doc if i.text != "_"]

        # updating head (ignoring '_')
        heads = [
            x.index(i) if i.head.text == "_" else x.index(i.head)
            for i in x
        ]

        # create new doc
        doc_new = spacy.tokens.Doc(
            nlp.vocab,
            [i.text for i in x],
            spaces=([True] * (len(x) - 1)) + [False],
            heads=heads,
            deps=[i.dep_ for i in x],
            sent_starts=[i.is_sent_start for i in x],
        )
        db_new.add(doc_new)
    db_new.to_disk(fp)
