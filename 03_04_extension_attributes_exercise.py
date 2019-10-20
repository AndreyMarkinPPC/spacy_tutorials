import spacy 
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_md")
matcher = PhraseMatcher(nlp.vocab)
doc = nlp("Czech Republic may help Slovakia protect its airspace and Russia supports that decison")


def countries_component(doc): 
    # create an entity span with the label "GPE"
    doc.ents = [Span(doc, start, end, label = nlp.vocab.strings["GPE"])
                for match_id, start, end in matcher(doc)]
    return doc

# add the component to the pipeline
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# Define dictionary with counties and capitals
capitals = {"Czech Republic": "Prague", 
            "Russia": "Moscow", 
            "Slovakia": "Lublana", 
            "Ireland": "Dublin"}

# getter that looks up the span text in the dictionary of capitals
get_capital = lambda span: capitals.get(span.text)

# register the span extension
Span.set_extension("capital", getter = get_capital)

# process the text and print the entity text, label, and capital
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])

