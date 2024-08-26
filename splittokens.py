import spacy
import tqdm
import presque


nlp = spacy.load("./model")

pr = presque.Normalizer(nlp)

d = "./docbin/"

for dataset in ("train", "dev", "test"):
    fp = d + dataset + ".spacy"
    print('current:', fp)
    db = spacy.tokens.DocBin()
    db_new = spacy.tokens.DocBin()
    db.from_disk(fp)
    for doc in tqdm.tqdm(db.get_docs(nlp.vocab)):
        doc_new = spacy.tokens.Doc(
            nlp.vocab,
            [i.text for i in doc],
            heads=[i.head.i for i in doc],
            deps=[i.dep_ for i in doc],
            spaces=([True] * (len(doc) - 1)) + [False],
        )
        for i in doc_new:
            i.norm_ = pr.normaliser_mot(i.text)
        db_new.add(doc_new)
    db_new.to_disk(fp)
