'''
spacy can compare two objects and predict their similarity - score between 0 and 1
can be Doc, Span, Token
via .similarity() method, takes another object as an argument
need a larger spacy model - medium or large
'''

import spacy

# load a larger model with vectors
nlp = spacy.load("en_core_web_md")

# compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print("Similarity between sentences:")
print(doc1.similarity(doc2))

# compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print("Similarity between tokens:")
print(token1.similarity(token2))

# compare a document and a token
doc = nlp("I like pizza")
token = nlp("soap")[0]
print("Similarity between doc and token:")
print(doc.similarity(token))

# compare a span and a document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")
print("Similarity between span and document:")
print(span.similarity(doc))

'''
similarity is determined by word vectors - multi-dimensional representation of words
default - cosine similarity, can be adjusted
Doc and Span vectors default to average of token vectors
Short phrases are better than long documents with many irrelevant words
'''

# access the vector via the token.vector attribute
print(doc[2].vector)
# result - 300 dimensional vector
