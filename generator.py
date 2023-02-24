import nltk
from nltk.tokenize import word_tokenize
nltk.download('universal_tagset')

# ----------------------- DEFINE A GRAMMAR ----------------------- 
grammar = r'''
    NP: {<DET>?<ADJ>*<NOUN>} # Noun phrase
    VP: {<VERB.*>+<ADV>?} # Verb phrase
'''

# ----------------------- DRAWING A TREE ----------------------- 
def draw_syntactic_tree(sentence):
    # tag the sentence with universal tokenizer (it's more general and readable)
    tagged = nltk.pos_tag(word_tokenize(sentence), tagset='universal')
    # create a parser based on the grammar
    cp = nltk.RegexpParser(grammar)
    # create a tree parsing the tag sentence with the parser
    result = cp.parse(tagged)
    # draw the tree
    result.draw()

# ----------------------- TESTING ----------------------- 
draw_syntactic_tree("""At eight o'clock on Thursday morning Arthur didn't feel very good.""")
draw_syntactic_tree("""I am waking up.""")
draw_syntactic_tree("""Mike is working at the trainstation.""")

draw_syntactic_tree("""Sweet are the uses of adversity which, like the toad, ugly and venomous, wears yet a precious jewel in his head.""")
