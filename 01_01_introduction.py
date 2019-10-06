#Import the english language class 
from spacy.lang.en import English

# instantite it
nlp = English()

# nlp contains 
# the preprocessing pipeline
# includes language specific rules for tokenization

# when you process a text with nlp object spacy creates a doc object
# allows you to access information about the text in a structured way
doc = nlp("Hello world 13!")

# iterate over tokens in doc
for token in doc: 
    print(token.text)

# token object represent the tokens in a documents (i.e., word)
# can get token at a specific position in a doc via indexing
print(doc[1])

# can access different information about token via: 
# .text

# Span object - a slice of the documents consisting of one or more tokens
#  create span with slice
span = doc[1:4]

# lexical attributes
# index - .i
print("Index: ", [token.i for token in doc])
print("Text: ", [token.text for token in doc])
print("is_alpha: ", [token.is_alpha for token in doc])
print("is_punct: ", [token.is_punct for token in doc])
print("like_num: ", [token.like_num for token in doc])

