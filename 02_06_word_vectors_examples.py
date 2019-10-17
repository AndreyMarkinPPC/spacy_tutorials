import spacy

nlp = spacy.load("en_core_web_md")
doc = nlp("Two bananas in pyjamas")

# get the vector for the token bananas
bananas_vector = doc[1].vector
print(bananas_vector)
# comparing similarities
doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's a sunny outside")

# get the similarity between two docs
similarity = doc1.similarity(doc2)
print("Similarity between two docs:")
print(similarity)

# similarity between tokens
doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

print("Similarity between tokens:")
print(token1.similarity(token2))

# similirity between spans
doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")
span1 = doc[3:5]
span2 = doc[12:15]

print("Similarity between spans:")
print(span1.similarity(span2))
