'''
What happens when we call nlp() on text to convert it to Doc:
1. the tokenizer is applied to turn the string in to a Doc object
2. a series of pipeline components is applied to the doc in order 
    (tagger, parser, ner, etc.)
3. the processed Doc is returned

Built-in pipeline components: 
    1. tagger - POS, creates: 
        1.1. Token.tag
    2. parser - Dependency parser, creates: 
        2.1. Token.dep
        2.2. Token.head
        2.3. Doc.sents
        2.4. Doc.noun_chunks
    3. ner - Named entity recognizer, creates: 
        3.1. Doc.ents
        3.2. Token.ent_iob
        3.3. Token.ent_type
    4. textcat - Text classifier, creates: 
        4.1. Doc.cats

all models you load into spacy include several files and a meta JSON.
The meta defines the language and pipeline - which components to instantiate
Built-in components need binary data to make predictions - data is included 
in the model package and loaded into the component when you load the model.

To see the names of the pipeline components present in the current nlp object,
you can use nlp.pipe_names attribute.
For a list of component names and component function tuples, you can user the 
nlp.pipeline attribute. 
'''

import spacy
nlp = spacy.load("en_core_web_sm")

# print the names of pipeline components
print(nlp.pipe_names)

# print the full pipeline of (name, component) tuples
print(nlp.pipeline)

################################################################################
# Custom pipeline components #
################################################################################

'''
let you add your own function to the spacy pipeline that is executed when you 
call the nlp object on a text - to modify the Doc and add more data to it.

After the text is tokenized and a Doc object has been created, pipeline 
components are appliced in order. 
Custom components are executed automatically when you call the nlp object on 
a text and useful for adding your own custom metadata to documents and tokens.
Can use them on update built-in attributed, like the named-entity spans. 

A pipeline component is a function that takes a doc, modifies it, so it can be
processed by the next component in the pipeline.

Components can be added to the pipeline via nlp.add_pipe(custom_component)
method.

You can specify where to add the component: 
    1. last - nlp.add_pipe(component, last = True)
    2. first - nlp.add_pipe(component, first = True)
    3. before - nlp.add_pipe(component, before = 'ner')
    4. after - nlp.add_pipe(component, after = 'tagger')

'''

def custom_component(doc):
    # print the doc's length
    print("Doc length:", len(doc))
    # return the doc object
    return doc

# add component to the pipeline
nlp.add_pipe(custom_component, first = True)

# print the pipeline component names
print("Pipeline:", nlp.pipe_names)

# process the text
doc = nlp("Hello world")
