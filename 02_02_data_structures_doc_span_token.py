'''
Doc object has two important views - Token and Span

Doc created automatically when you process a text with nlp object
'''

import spacy
from spacy.lang.en import English
nlp = English() 
doc = nlp("Some text")

# you can instantiate class manually

from spacy.tokens import Doc

words = ["Hello", "world", "!"]
spaces = [True, False, False]

'''
Doc class takes three arguments: 
    1. the shared vocab - nlp.vocab
    2. the words
    3. the spaces
'''

doc = Doc(nlp.vocab, words = words, spaces = spaces)

'''
Span - slice of a Doc consisting of one or more tokens
It takes at least three arguments: 
    1. the doc it refers to
    2. start index of the span
    3. end index of span

To create a span manually
'''

from spacy.tokens import Doc, Span
words = ["Hello", "world", "!"]
spaces = [True, False, False]
doc = Doc(nlp.vocab, words = words, spaces = spaces)
span = Span(doc, 0, 2)


# We can add an entity label to the span
# span_with_label = Span(doc, 0, 2, label = "GREET")

# the doc ents are writable, so we can add entities manually by overwriting it with a list of spans

# doc.ents = [span_with_label]
