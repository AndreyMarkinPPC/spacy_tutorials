import spacy

# load model
nlp = spacy.load("en_core_web_sm")
text = "It's official: Apply is the first U.S. public company to reach a $1 trillion market value"

# process the text
doc = nlp(text)

print("====== printing the source text =====")
# print the text
print(doc.text)

print("===== printing NER results =====")
# predict linguistic annotations
for ent in doc.ents: 
    # print the entity and its label
    print(ent.text, ent.label_)

print("====== printing POS tags and dependency labels =====")
# print pos-tags
for token in doc: 
    # get token text, pos tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # perform formatting
    print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))
    

# predict named entities in context

text = "New iPhone X release date leadked as Apple reveals pre-orders by mistake"

# process the text
doc = nlp(text)

# iterate over entities
for ent in doc.ents: 
    # print entity and label
    print(ent.text, ent.label_)

# get span for "iPhone X"
iphone_x = doc[1:3]

print("===== printing missing entity =====")
# print the span text
print("Missing entity: ", iphone_x.text)


