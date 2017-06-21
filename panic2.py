phrase = 'Dont panic!'
plist = list(phrase)
print phrase
print plist





# for letter in range(4):
#     plist.pop()

# plist.pop(0)

# plist.insert(2, plist.pop(3))

# plist.extend([plist.pop(), plist.pop()])

new_phrase = ''.join(plist[1:3])

new_phrase = new_phrase + plist[4] + plist[3] + plist[6] + plist[5]

print plist
print new_phrase
