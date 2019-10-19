import spacy
from spacy.matcher import Matcher
from spacy.lang.en import English
nlp = English()
doc = nlp('Twitch Prime, the perks program for Amazon Prime members offering free loot, games and other benefits, is ditching one of its best features: ad-free viewing. According to an email sent out to Amazon Prime members today, ad-free viewing will no longer be included as a part of Twitch Prime for new members, beginning on September 14. However, members with existing annual subscriptions will be able to continue to enjoy ad-free viewing until their subscription comes up for renewal. Those with monthly subscriptions will have access to ad-free viewing until October 15.')

# match all case-insensitive mentions of amazon plus a title cased proper noun
pattern1 = [{"LOWER": "amazon"},
            {"IS_TITLE": True, "POS": "PROPN"}]

# Initialize the matcher and add the pattens
pattern2 = [{'LOWER': 'ad'}, {"TEXT":"-"}, {'LOWER': 'free'}] 
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", None, pattern1)
matcher.add("PATTERN2", None, pattern2)

# Iterate over the matches
for match_id, start, end in matcher(doc): 
    print(doc[start:end].text)
