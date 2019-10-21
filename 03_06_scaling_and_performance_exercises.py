import spacy
nlp = spacy.load("en_core_web_sm")

TEXTS = ['McDonalds is my favorite restaurant.',
          'Here I thought @McDonalds only had precooked burgers but it seems they only have not cooked ones?? I have no time to get sick..',
          'People really still eat McDonalds :(',
          'The McDonalds in Spain has chicken wings. My heart is so happy ',
          '@McDonalds Please bring back the most delicious fast food sandwich of all times!!....The Arch Deluxe :P',
          'please hurry and open. I WANT A #McRib SANDWICH SO BAD! :D',
          'This morning i made a terrible decision by gettin mcdonalds and now my stomach is payin for it']

for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])

# process text and print the entities
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print( *entities)

################################################################################
# Add context
################################################################################

from spacy.tokens import Doc
Doc.set_extension("book", default = None)
Doc.set_extension("author", default = None)

DATA = [('One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.',
           {'author': 'Franz Kafka', 'book': 'Metamorphosis'}),
         ("I know not all that may be coming, but be it what it will, I'll go to it laughing.",
            {'author': 'Herman Melville', 'book': 'Moby-Dick or, The Whale'}),
         ('It was the best of times, it was the worst of times.',
            {'author': 'Charles Dickens', 'book': 'A Tale of Two Cities'}),
         ('The only people for me are the mad ones, the ones who are mad to live, mad to talk, mad to be saved, desirous of everything at the same time, the ones who never yawn or say a commonplace thing, but burn, burn, burn like fabulous yellow roman candles exploding like spiders across the stars.',
            {'author': 'Jack Kerouac', 'book': 'On the Road'}),
         ('It was a bright cold day in April, and the clocks were striking thirteen.',
            {'author': 'George Orwell', 'book': '1984'}),
         ('Nowadays people know the price of everything and the value of nothing.',
            {'author': 'Oscar Wilde', 'book': 'The Picture Of Dorian Gray'})]

for doc, context in nlp.pipe(DATA, as_tuples = True):
    doc._.book = context["book"]
    doc._.author = context["author"]

    print(doc.text, "\n", "- '{}' by {}".format(doc._.book, doc._.author), "\n")


################################################################################
# Use only tokenizer 
################################################################################
text = "Some random text here that goes on and on and on and on..."
with nlp.disable_pipes("tagger", "parser"): 
    doc = nlp(text)
    print(doc.ents)


