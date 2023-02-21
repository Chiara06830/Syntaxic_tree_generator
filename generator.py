import nltk
from nltk.tokenize import word_tokenize
nltk.download('universal_tagset')

grammar = r'''
    NP: {<DET>?<ADJ>*<NOUN>}
    VP: {<VERB.*>+<ADV>?}
'''

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tagged = nltk.pos_tag(word_tokenize(sentence), tagset='universal')

cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged)

result.draw()
