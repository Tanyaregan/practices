
def plaintext(encoded):
    """Takes an encoded string and returns decoded phrase.

    >>> plaintext('0h2abe1zy')
    'hey'

    >>> plaintext('0h2zyi2467')
    'hi'

    >>> plaintext('0h2zyi24*67')
    Sorry, that is not encoded properly. Letters and numbers only.
    ''
    """

    index = 0
    decoded = ''

    # Check to make sure encoded string is formatted correctly for decode,
    # return empty and quit if there are any non alphanumeric characters
    for char in encoded:
        if not char.isalpha() and not char.isdigit():
            print 'Sorry, that is not encoded properly. Letters and numbers only.'
            return ''
            break


    while index < (len(encoded)):

        # the char index indicator number
        indexed_num = int(encoded[index])

        # the index where the char can be found
        index_position = index + indexed_num + 1

        # The char at the indexed_num in the string
        indexed_char = encoded[index_position]
        # if the resulting char is not a letter, quit
        if not indexed_char.isalpha():
            break

        # adds the indexed char to the decoded string
        decoded += indexed_char

        # increases index to the index of next character after indexed_char
        index = index_position + 1

    return decoded

if __name__ == "__main__":

    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print 'All tests passed!'
