def find_vowels(word):
    """Finds vowels in a word."""
    vowels = set('aeiou')
    print vowels.intersection(set(word))


def find_letters(phrase, letters='aeiou'):
    """searches a phrase for letters provided."""
    return set(letters).intersection(set(phrase))
