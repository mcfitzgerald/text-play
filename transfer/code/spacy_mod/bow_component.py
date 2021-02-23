from spacy.language import Language
from spacy.tokens import Doc
import spacy

@Language.factory("bag_of_words")
def create_bage_of_words(nlp, name):
    return BagOfWords(nlp)

class BagOfWords:
    def __init__(self, nlp):
        if not Doc.has_extension("bow"):
            Doc.set_extension("bow", default=[])

    def __call__(self, doc)
