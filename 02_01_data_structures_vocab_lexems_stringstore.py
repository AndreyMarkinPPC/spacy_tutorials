'''
Spacy stores all shared data in a vocabulary - Vocab
stores data shared across multiple documents
includes words, lables, schemes for tags and entities

To save memory, spacy encodes all strings to hash values
it uses a hash function to generate Id and  store the string
only once in the string store

The StringStore is available as nlp.vocab.strings
It's a lookup table that works in both directions

coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

Internally spacy communities only with hash ids

To get the hash for a string, we can look it up in nlp.vocab.strings

'''

import spacy
from spacy.lang.en import English
nlp = English()
import spacy

doc = nlp("I love coffee")

print("hash value: ", nlp.vocab.strings["coffee"])
print("string value: ", nlp.vocab.strings[3197928453018144401])

# doc object also exposes the vocab and strings
print("hash value: ", doc.vocab.strings["coffee"])

'''
lexems are  context-independent entries in the vocabulary

you can get a lexeme by looking up a string or a hash id in the vocab
They expose attributes, just like tokens
and hold information about a word like a text or alpha numeric character
don't have POS tags, dependencies or entity labels
'''

lexeme = nlp.vocab["coffee"]

# print the lexical attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)

print("===================")

person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

person_string = nlp.vocab.strings[person_hash]
print(person_string)
