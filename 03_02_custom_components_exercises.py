import spacy 
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.lang.en import English

nlp = spacy.load("en_core_web_md")
animal_patterns = ["Golden Retriever", 
                   "cat", "turtle", 
                   "Rattus norvegicus"]
patterns = list(nlp.pipe(animal_patterns))
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMALS", None, *patterns)

# define custom component
def animal_component(doc): 
    # create span for each match and assign label animal
    # and overwrite the doc.ents with the matched spans
    doc.ents = [Span(doc, start, end, label = nlp.vocab.strings["ANIMAL"])
                for match_id, start, end in matcher(doc)]
    return doc

# add the component to the pipeline after the ner component
nlp.add_pipe(animal_component, after = 'ner')

# process the text and print the text and label for the doc.ents
doc = nlp('I have a cat and a Golden Retriever')
print([(ent.text, ent.label_) for ent in doc.ents])
