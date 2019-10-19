from spacy.matcher import PhraseMatcher
from spacy.lang.en import English
from spacy.tokens import Span
nlp = English()
matcher = PhraseMatcher(nlp.vocab)
COUNTRIES = ["Spain", "Portugal", "Slovakia", "Czech Republic", "Namibia", "South Africa", 
            "Cambodia", "Kuwait", "Somalia", "Haiti", "Mozambique", 
            "Rwanda", "Singapore", "Russia", "France", "Iraq", "Afganistan", 
            "Sudan", "Congo", "Haiti"]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

doc = nlp("Czech Republic may help Slovakia protect its airspace")

matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])

# Geo-political entities
doc = nlp('After the Cold War, the UN saw a radical expansion in its peacekeeping duties, taking on more missions in ten years than it had in the previous four decades.Between 1988 and 2000, the number of adopted Security Council resolutions more than doubled, and the peacekeeping budget increased more than tenfold. The UN negotiated an end to the Salvadoran Civil War, launched a successful peacekeeping mission in Namibia, and oversaw democratic elections in post-apartheid South Africa and post-Khmer Rouge Cambodia. In 1991, the UN authorized a US-led coalition that repulsed the Iraqi invasion of Kuwait. Brian Urquhart, Under-Secretary-General from 1971 to 1985, later described the hopes raised by these successes as a "false renaissance" for the organization, given the more troubled missions that followed. Though the UN Charter had been written primarily to prevent aggression by one nation..')

for match_id, start, end in matcher(doc):
    # create span with the label "GPE" and overwrite the doc.ents
    span = Span(doc, start, end, label = nlp.vocab.strings["GPE"])
    doc.ents = list(doc.ents) + [span]

    # get the span's root head token
    span_root_head = span.root.head
    # print the text of span's root head token and the span text
    print(span_root_head.text, "--->", span.text)

print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])


