from spacy import registry
from spacy.tokens import Doc


class BlankTokenizer:
    def __init__(self, vocab, *args, **kwargs):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split()
        words = [i.strip() for i in words if i.split() != ""]
        spaces = [True] * len(words)
        return Doc(self.vocab, words, spaces)

    def to_disk(self, path, *, exclude=tuple()):
        pass

    def from_disk(self, path, *, exclude=tuple()):
        pass


@registry.callbacks("space_tokenizer")
def make_space_tokenizer():
    def space_tokenizer(nlp):
        nlp.tokenizer = BlankTokenizer(nlp.vocab)
    return space_tokenizer
