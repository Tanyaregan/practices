# counts = {}

# names = ('joe', 'john', 'sally', 'sally', 'joe', 'kelly', 'john', 'john', 'kelly', 'joe', 'joe', 'joe')

# for name in names:
#         counts[name] = counts.get(name, 0) + 1

# name_repeats = 0
# actual_name = ''

# for name in counts:
#     if counts[name] > name_repeats:
#         name_repeats = counts[name]
#         actual_name = name

# print actual_name, 'is the most common name, appearing', name_repeats, 'times.'

# print counts.get('jackass', 'there is no jackass, jackass')

# dictionary = {}
# listy = [1, 2, 3, 4, 5, 6, 7, 7, 8, 5, 6, 4, 4, 4, 4, 4]

# for num in listy:
#     dictionary[num] = dictionary.get(num, 0) + 1

# print dictionary

# key_num = 0
# highest_num = 0

# for num in dictionary:
#     if dictionary[num] > highest_num:
#         highest_num = dictionary[num]
#         key_num = num

# print key_num, 'appears the most:', highest_num, 'times.'

# dictionary = {}
# phrase = raw_input('Enter a phrase: ')
# words = phrase.split()

# for word in words:
#     dictionary[word] = dictionary.get(word, 0) + 1

# most_common = ''
# frequency = 0

# for word in dictionary:
#     if dictionary[word] > frequency:
#         frequency = dictionary[word]
#         most_common = word

# print 'number of words is', len(words)
# print 'most common word is', most_common
# print most_common, 'appeared', frequency, 'times in the phrase.'

# file_handle = open('data.txt')
# text = file_handle.read()
# words = text.split()

# words_dict = {}

# for word in words:
#     words_dict[word] = words_dict.get(word, 0) + 1

# most_word = None
# freq = None

# for word, num in words_dict.items():
#     if most_word is None or num > freq:
#         freq = num
#         most_word = word

# print word, 'appears the most times:', freq, 'times.'

handle = open("mbox.txt")

emails_dict = {}
freq = None
address = None

for line in handle:
    line = line.rstrip()
    if 'From' in line:
        email = line.split()
        emails_dict[(email[1])] = emails_dict.get(email[1], 0) + 1

for key, value in emails_dict.items():
    if address is None or value > freq:
        address = key
        freq = value

print address, freq
