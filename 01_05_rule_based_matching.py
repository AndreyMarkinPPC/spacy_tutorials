
## match lexical attributes
### [{"LOWER":"iphone"}, {"LOWER":"x"}]

## match any token attributes
### [{"LEMMA":"buy"}, {"POS":"NOUN"}]

# to use a pattern, we import matcher

import spacy
from spacy.matcher import Matcher

# load a model and create an nlp object
nlp = spacy.load("en_core_web_sm")

# Initiaize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# add a pattern to the matcher
pattern = [{"ORTH": "iPhone"}, {"ORTH":"X"}]

# three arguments
## 1. unique ID to identify which pattern was matched
## 2. optional callback
## 3. pattern
matcher.add("IPHONE_PATTERN", None, pattern)

# Process some text
doc = nlp("New iPhone X release date leaked")

# call the matcher on the doc
matches = matcher(doc)

# this will  return the matches - list of tuples
# each tuple consists of three values: 
## 1. match id
## 2. start index
## 3. end index of the matched span

for match_id, start, end in matches: 
    # get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

# more complex pattern
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

doc = nlp("2018 FIFA World cup: France won!")

matcher.add("FIFA_", None, pattern)
matches = matcher(doc)

for match_id, start, end in matches: 
    matched_span = doc[start:end]
    print(matched_span.text)


# another pattern
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]

doc = nlp("I loved dogs but now I love cats more.")

matcher.add("ANIMALS_", None, pattern)
matches = matcher(doc)

for match_id, start, end in matches: 
    matched_span = doc[start:end]
    print(matched_span.text)

# Using operators and quantifies
pattern = [
    {"LEMMA": "buy"},
    {"POS" : "DET", "OP" : "?"},
    {"POS" : "NOUN"}
]

## ? - makes the determiner token optional - match 0 or 1 times
doc = nlp("I bought a smartphone. Now I'm buying apps.")
matcher.add("APPS_", None, pattern)
matches = matcher(doc)

for match_id, start, end in matches: 
    matched_span = doc[start:end]
    print(matched_span.text)

# Operators
## ! - match 0 times
## ? - 0 or 1 times
## + - 1 or more times
## * - 0 or more times
