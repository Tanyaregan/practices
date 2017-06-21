phrase = 'Dont panic!'
plist = list(phrase)
print phrase
print plist

for letter in range(4):
    plist.pop()

plist.pop(0)

plist.insert(2, plist.pop(3))

plist.extend([plist.pop(), plist.pop()])

new_phrase = ''.join(plist)
print plist
print new_phrase
