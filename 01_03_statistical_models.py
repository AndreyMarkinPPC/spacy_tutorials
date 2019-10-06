# enable spaCy to predict linguistic attributes in context
## POS-tagging
## Syntactic dependencies
## Named entities

# trained on labeled example texts
# can be update with more examples to fine-tune predictions

import spacy

# load model
nlp = spacy.load("en_core_web_sm")

# inside package
## binary weights 
## vocabulary
## meta information - language, pipeline

# process the text
doc = nlp("She ate the pizza")

print("===== printing POS tags =====")
for token in doc: 
    # print the text and the predicted POS tag
    # attributes with _ returns an attribute, without - id
    print(token.text, token.pos_)

# predicting syntactic dependencies
## use dep_ - returns predicted dependency label
## head attribute returns the syntactic head token - patern token it's attached to
print("===== printing dependency tags =====")
for token in doc: 
    print(token.text,  token.pos_, token.dep_, token.head.text)

# Predicting named entities
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

# ents allows you to access entities 
# returns an iterator of Span objects
print("===== printing NERs =====")
for ent in doc.ents: 
    # print entity text and its label
    print(ent.text, ent.label_)

# use spacy.explain("") to get definitions of NER
print("====== Spacy explanation =====")
print(spacy.explain("GPE"))
