"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    words = contents.split()

    return words

#print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
        
    """
    chains = {}
    
    for i in range(len(text_string) - 3):
        #6 elements len(string) = 6 - 3
        #0-5 indices
        #3 index is the last one 
        key = (text_string[i], text_string[i + 1])
        current_value = (text_string[i + 2])

        if key not in chains:
            chains[key] = [current_value]
        else:
            
            chains[key].append(current_value)
            
    return chains
print(make_chains(['Would', 'you', 'could', 'you', 'in', 'a', 'house?', 'Would', 'you', 'could', 'you', 'with', 'a', 'mouse?', 'Would', 'you', 'could', 'you', 'in', 'a', 'box?', 'Would', 'you', 'could', 'you', 'with', 'a', 'fox?', 'Would', 'you', 'like', 'green', 'eggs', 'and', 'ham?', 'Would', 'you', 'like', 'them,', 'Sam', 'I', 'am?']))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
