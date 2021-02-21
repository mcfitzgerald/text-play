from typing import List, Dict, Union
from spacy.tokens import Doc, Token
from spacy.matcher import Matcher
from srsly import read_json


class FilterTextPreprocessing:
    def __init__(self, nlp, patterns: List[Dict[str, Union[str, List[Dict]]]]):
        Doc.set_extension("bow", default=[])
        Token.set_extension("keep", default=True)

        self.matcher = Matcher(nlp.vocab)

        for patt_obj in patterns:
            string_id = patt_obj.get("string_id")
            pattern = patt_obj.get("pattern")
            self.matcher.add(string_id, pattern)

    def on_match(self, matcher, doc, i, matches):
        _, start, end = matches[i]
        for tkn in doc[start:end]:
            tkn._.keep = False

    def __call__(self, doc):
        self.matcher(doc)
        doc._.bow = [tkn.text for tkn in doc if tkn._.keep]
        return doc

    @classmethod
    def from_pattern_file(cls, nlp, path):
        patterns = read_json(path)
        return cls(nlp, patterns)
