vowels = ['a', 'e', 'i', 'o', 'u']
word = raw_input('Gimme a word, plz: ')
found = {
'a' : 0,
'e' : 0,
'i' : 0,
'o' : 0,
'u' : 0}

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print vowel

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found[letter] = 1
#         else:
#             found[letter] += 1

for letter in word:
    if letter in found:
        found[letter] += 1

# for key in sorted(found):
#     if found[key] != 0:
#         print 'there are', found[key], 'occurances of the vowel', key

for k, v in sorted(found.items()):
    if v > 0:
        print 'found', v, 'instances of the letter', k