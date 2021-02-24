import spacy
from spacy.language import Language
from spacy.tokens import Doc

@Language.factory("bag_of_words")
def create_bag_of_words(nlp, name):
    return BagOfWords(nlp)

class BagOfWords:
    def __init__(self, nlp):
        if not Doc.has_extension("bow"):
            Doc.set_extension("bow", default=[])

    def __call__(self, doc):
        for token in self.simple_clean(doc):
            doc._.bow.append(token)
        return doc
    
    def simple_clean(self, doc):
        '''
        Removes stopwords and punctuation and 
        returns lemms using spaCy builtins
        '''
        for token in doc:
            if not token.is_space:
                if not token.is_punct:
                    if not token.is_stop:
                        yield token.lemma_