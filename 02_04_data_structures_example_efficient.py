import spacy
from spacy.lang.en import English
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")

doc = nlp("Berlin is a nice city")
for token in doc: 
    # check if the current token in a proper noun
    if token.pos_ == "PROPN":
        # check if the next token is a verb
        if doc[token.i + 1].pos_ == "VERB": 
            print("Found a verb after a proper noun!")
            print("Phrase: %s %s" % (token.text, doc[token.i + 1].text))


