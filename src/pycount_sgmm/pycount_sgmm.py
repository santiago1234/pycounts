from collections import Counter
from string import punctuation


def load_text(input_file):
    """Loads text file

    Loads text file

    Args:
        input_file (str): path to input file
    """
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text
    
def count_words(input_file):
    """Count unique words in a string."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
