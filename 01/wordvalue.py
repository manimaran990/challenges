from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
    	return [ word.strip() for word in f.readlines() ]
    		

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum( LETTER_SCORES.get(l, 0) for l in word.upper() )

def max_word_value(list_word=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = list_word
    if list_word is None:
    	words = load_words()

    lst = [ (w, calc_word_value(w)) for w in words ]
    lst.sort(reverse=True, key=lambda x: x[1])
    return lst[0][0]
    


if __name__ == "__main__":
    pass # run unittests to validate
