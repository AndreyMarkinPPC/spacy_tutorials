'''
add custom attributes to Doc, Token, and Span objects to store custom metadata
custom attributes are available via ._ property.

doc._.title = "My document"
token._.is_colour = True
        colors = ["red", "yellow", "blue"]
        return any(token.text in colors for token in span)


    3. method extrensions - make the extension attribute a callable method.
    you can pass aurguments to the extension function

    def has_token(doc, token_text): 
        in_doc = token_text in [token.text for token in doc]

    Doc.set_extension("has_token", method = has_token)
    print(doc._.has_token("blue"))

'''

from spacy.tokens import Doc, Span, Token
from spacy.lang.en import English

nlp = English()
# register a token extension attribute 'is_country' with the default value False
Token.set_extension("is_country", default = False)

# process text and set is_country attribute to True for the token "Spain"
doc = nlp("I live in Spain")

doc[3]._.is_country = True

# print the token text and is_country attribute for all tokens
print([(token.text, token._.is_country) for token in doc])

################################################################################
# Reversed token
################################################################################


# define the getter function that returns reversed token
def get_reversed(token):
    return token.text[::-1]

# register the token property with getter
Token.set_extension("reversed", getter = get_reversed)

# process a text
doc = nlp("All generalizations are false, including this one")
print("#####################################################")

for token in doc: 
    print("reversed", token._.reversed)

################################################################################
# Document has number
################################################################################


def get_has_number(doc): 
    # return if any of the tokens in the doc is a number
    return any(token.like_num for token in doc)

# register doc property extension
Doc.set_extension("has_number", getter = get_has_number)

# process the text
doc = nlp("The museum close for five years in 2012")
print("#####################################################")
print("has number:", doc._.has_number)

################################################################################
# span has html tagg 
################################################################################

def to_html(span, tag):
    # wrap the span text in a HTML tag a return it
    return "<{tag}>{text}</{tag}>".format(tag = tag, text = span.text)


# register the span property extension with method
Span.set_extension("to_html", method = to_html)

doc = nlp("Hello world, this is a sentence")
span =doc[0:2]
print("#####################################################")
print(span._.to_html("strong"))

################################################################################
# span has html tagg 
################################################################################
import spacy

nlp = spacy.load("en_core_web_sm")
def get_wikipedia_url(span):
    # get wikipedia url if the span has one of the labels
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text

# set the span extension
Span.set_extension("wikipedia_url", getter = get_wikipedia_url)

doc = nlp("In over fifty years from his very first recordings right through to his last album, David Bowie was at the vanguard of contemporary culture.")
print("#####################################################")
for ent in doc.ents: 
    print(ent.text, ent._.wikipedia_url)
