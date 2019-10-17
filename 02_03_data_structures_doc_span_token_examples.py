from spacy.tokens import Doc, Span
from spacy.lang.en import English

nlp = English()

# Create doc
doc = Doc(nlp.vocab, 
          words = ["I", "like", "David", "Bowie"],
          spaces = [True, True, True, False]
         )
print(doc)
# create span for David Bowie
span = Span(doc, 2, 4, label=nlp.vocab.strings["PERSON"])

# add span to doc entities
doc.ents = [span]

# print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])
