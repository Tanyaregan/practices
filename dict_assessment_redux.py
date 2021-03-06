"""Dictionaries Assessment
**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

from random import choice

# def count_words(phrase):
#     """Count unique words in a string.
#     This function should take a single string and return a dictionary
#     that has all of the distinct words as keys and the number of
#     times that word appears in the string as values.
#     For example::
#         >>> print_dict(count_words("each word appears once"))
#         {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
#     Words that appear more than once should be counted each time::
#         >>> print_dict(count_words("rose is a rose is a rose"))
#         {'a': 2, 'is': 2, 'rose': 3}
#     It's fine to consider punctuation part of a word (e.g., a comma
#     at the end of a word can be counted as part of that word) and
#     to consider differently-capitalized words as different::
#         >>> print_dict(count_words("Porcupine see, porcupine do."))
#         {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
#     """

#     phrase_dict = {}
#     phrase_list = phrase.split()

#     for word in phrase_list:
#         if word in phrase_dict:
#             phrase_dict[word] += 1
#         else:
#             phrase_dict[word] = 1

#     return phrase_dict


# def get_melon_price(melon_name):
#     """Given a melon name, return the price of the melon.
#     Here are a list of melon names and prices:
#     Watermelon 2.95
#     Cantaloupe 2.50
#     Musk 3.25
#     Christmas 14.25
#     (it was a bad year for Christmas melons -- supply is low!)
#     If melon name does not exist, return 'No price found'.
#         >>> get_melon_price('Watermelon')
#         2.95
#         >>> get_melon_price('Musk')
#         3.25
#         >>> get_melon_price('Tomato')
#         'No price found'
#     """

#     melon_dict = {'Watermelon': 2.95, 'Cantaloupe': 2.50, 'Musk': 3.25, 'Christmas': 14.25}

#     if melon_name not in melon_dict:
#         return 'No price found.'
#     else:
#         return melon_dict[melon_name]


# def word_length_sorted(words):
#     """Return list of word-lengths and words.
#     Given a list of words, return a list of tuples, ordered by
#     word-length. Each tuple should have two items --- a number that
#     is a word-length, and the list of words of that word length.
#     In addition to ordering the list by word length, order each
#     sub-list of words alphabetically.
#     For example::
#         >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
#         >>> word_length_sorted(["porcupine", "ok"])
#         [(2, ['ok']), (9, ['porcupine'])]
#     """

#     word_length_dict = {}

#     for word in words:
#         if word not in word_length_dict:
#             word_length_dict[word] = 1
#         else:
#             word_length_dict[word] += 1

#     return sorted(word_length_dict.items())


# def translate_to_pirate_talk(phrase):
#     """Translate phrase to pirate talk.
#     Given a phrase, translate each word to the Pirate-speak
#     equivalent. Words that cannot be translated into Pirate-speak
#     should pass through unchanged. Return the resulting sentence.
#     Here's a table of English to Pirate translations:
#     ----------  ----------------
#     English     Pirate
#     ----------  ----------------
#     sir         matey
#     hotel       fleabag inn
#     student     swabbie
#     man         matey
#     professor   foul blaggart
#     restaurant  galley
#     your        yer
#     excuse      arr
#     students    swabbies
#     are         be
#     restroom    head
#     my          me
#     is          be
#     ----------  ----------------
#     For example::
#         >>> translate_to_pirate_talk("my student is not a man")
#         'me swabbie be not a matey'
#     You should treat words with punctuation as if they were different
#     words::
#         >>> translate_to_pirate_talk("my student is not a man!")
#         'me swabbie be not a man!'
#     """

#     pirate_english_dict = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie',
#     'man': 'matey', 'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer',
#     'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'restroom': 'head', 'my': 'me',
#     'is': 'be'}

#     phrase = phrase.split()
#     pirate_phrase = []

#     for word in phrase:
#         if word in pirate_english_dict:
#             pirate_phrase.append(pirate_english_dict[word])
#         else:
#             pirate_phrase.append(word)

#     converted_phrase = ' '
#     translation = converted_phrase.join(pirate_phrase)

#     return translation



def kids_game(names):
    """Play a kids' word chain game.
    Given a list of names, like::
      bagon baltoy yamask starly nosepass kalob nicky
    Do the following:
    1. Always start with the first word ("bagon", in this example).
    2. Add it to the results.
    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".
    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.
    5. When you can't find an unused word to use, you're done!
       Return the list of output words.
    For example::
        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']
    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)
    Two more examples:
        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']
        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']
    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # make a list with the first name of names as the first item
    # make a dict for the names and their starting letters

    results = [(names[0])]
    starts_with = {}

    # populate the dict with the 1st letter as key,
    # all words that start with key letter as list values

    for name in names:
        if name[0] not in starts_with:
            starts_with[name[0]] = [name]
        else:
            starts_with[name[0]].append(name)

    while True:

        # key is the last letter of the last word in results list
        # get value list from dict using key, return None if there is no key

        key = results[-1][-1]
        value = starts_with.get(key, None)

        # if the value is not None, next_name is item[0],
        # pop from values list and append to results list
        # if value is None, the game is over

        if value != None:
            next_name = (starts_with[key]).pop(0)

            if next_name not in results:
                results.append(next_name)

            else:
                next_name = (starts_with[key]).pop(0)

        else:
            return results


print kids_game(["apple", "berry", "cherry"])
print kids_game(["noon", "naan", "nun"])

#####################################################################
#