'''
when you need statistical models: 
    * application needs to generalize based on examples
    * detect product or person names, subject/object relationship
    * corresponds to spacy features: NER, dependency parser, POS tagger
when you need rule-based systems: 
    * dictionary iwth finite number of examples
    * i.e., countries, dog breeds
    * corresponds to spacy features: tokenizer, Matcher, PhraseMatcher
'''

from spacy.matcher import Matcher
import spacy
nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

# patters are list of dictionaries
pattern = [{"LEMMA":"love", "POS":"VERB"},
           {"LOWER":"cats"}]

# add pattern via .add() method
# specify how ofter a token should be matched via operators
pattern = [{'TEXT': 'very', 'OP': '+'},
           {'TEXT': 'happy'}]

matcher.add("DOG", None, [{"LOWER": "golden"}, {"LOWER":"retriever"}])

doc = nlp("I have a Golden Retriever")



for match_id, start, end in matcher(doc): 
    span = doc[start:end]
    print("matched span:", span.text)
    # get more statistical infor
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    print("Previous token:", (doc[start - 1].text, doc[start - 1].pos_))


# Efficient phrase matching - find sequences of words in data
# Performance search like regexp but with access to the tokens
# Takes Doc object as patterns

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)
# pass doc object to it
pattern = nlp("Golden Retriever")
matcher.add("DOG", None, pattern)

doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
