import spacy
from spacy.matcher import Matcher

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# load a model
nlp = spacy.load("en_core_web_sm")
# initialize matcher
matcher = Matcher(nlp.vocab)

# create a pattern matching two tokens: "iPhone" and "X"
pattern = [
    {"ORTH": "iPhone"},{"ORTH": "X"}
]

# add pattern to the matcher
matcher.add("IPHONE_X_PATTERN", None, pattern)

doc = nlp(text)

# use the matcher on the doc
matches = matcher(doc)

print("matches: ", 
      [doc[start:end].text for match_id, start, end in matches])

# Writing match patters

## mentions of full iOS versions - iOS 7, iOS 11, etc
doc = nlp("After making the iOS update you won't notice a radical system-wide redesign: nothing like the aesthetic upheaval we got with iOS 7. Most of iOS 11's furniture remains the same as in iOS 10. But you will discover some tweaks once you delve a little deeper.")

pattern = [
    {"TEXT": "iOS"},
    {"IS_DIGIT": True}
]

matcher.add("IOS_VERSION_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found: " , len(matches))
print([doc[start:end].text for _, start, end in matches])

print("=========================")
# matching forms of "download"

doc = nlp("i downloaded Fortnite on my laptop and can't open the game at all. Help? so when I was downloading Minecraft, I got the Windows version where it is the '.zip' folder and I used the default program to unpack it... do I also need to download Winzip?")

pattern = [
    {"LEMMA": "download"},
    {"POS" : "PROPN"}
]

matcher.add("DOWNLOAD_", None, pattern)
matches = matcher(doc)

matches = matcher(doc)
print("Total matches found: " , len(matches))
print([doc[start:end].text for _, start, end in matches])
print("=========================")

# match adjectives followed by one or two nouns

doc = nlp("Features of the app include a beautiful design, smart search, automatic labels and optional voice responses.")

pattern = [
    {"POS" : "ADJ"},
    {"POS" : "NOUN"},
    {"POS" : "NOUN", "OP": "?"}
    ]

matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)

matches = matcher(doc)
print("Total matches found: " , len(matches))
print([doc[start:end].text for _, start, end in matches])
print("=========================")


