'''
To process large volumes of text use nlp.pipe method: 
    * it processes text as a stream
    * yields Doc objects
    * much faster than calling nlp on each text

Example: 
    docs = list(nlp.pipe(LOTS_OF_TEXTS))

Passing in context

nlp.pipe supports passing in tuples of text/contexts
via setting as_tuples = True
method yields (doc, context) tuples
useful for passing additional metadata, like id or page number
'''
import spacy
nlp = spacy.load("en_core_web_sm")

data = [
    ("This is a text", {"id":1, "page_number": 15}),
    ("This is another text", {"id": 2, "page_number": 16})
]

for doc, context in nlp.pipe(data, as_tuples = True): 
    print(doc.text, context["page_number"])

'''
Can add context meta data to custom attributes

After processing text and passing through context we can overwrite the 
doc extension with our context metadata
'''

from spacy.tokens import Doc
Doc.set_extension("id", default = None)
Doc.set_extension("page_number", default = None)

for doc, context in nlp.pipe(data, as_tuples = True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]

'''
Sometimes you only need tokenizer
use nlp.make_doc to turn text into a Doc object
'''

doc2 = nlp.make_doc("Hello world")

'''
Temporarily disable pipeline components via nlp.disable_pipes
'''

# you want to use only ner
with nlp.disable_pipes("tagger", "parser"): 
    doc = nlp("Moscow is a capital of Russia")
    print(doc.ents)

''' 
after with block all pipeline components will be restored
'''
