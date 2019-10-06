from spacy.lang.en import English

nlp = English()

doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. Now less than 4% are.")

# iteracte over tokens in a doc

for token in doc: 
    # check if tockens resembles a number
    if token.like_num: 
        # get the next token in the document
        next_token = doc[token.i + 1]
        if next_token.text == "%": 
            print("Percentage found:", token.text)
