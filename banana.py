fruit = 'banana'
fruity = 'APPLE'

index = 0
while index < len(fruit):
    print index, fruit[index]
    index += 1


for letter in fruit:
    print letter

n_count = 0
for letter in fruit:
    if letter == 'n':
        n_count += 1
print n_count, 'of the letter n in', fruit

count = 0
for letter in fruit:
    count += 1
print count, 'letters in', fruit

first_three = 0
for letter in fruit[:3]:
    print letter
    first_three += 1
print first_three, 'letters'

a_count = 0
for letter in fruit:
    if letter == 'a':
        a_count += 1

if 'a' in fruit:
    print 'Hell yes, there is an A in', fruit
    print 'as a matter of fact, there are', a_count

print fruit.upper()
print fruity.lower()

greet = "Hello    There "
greet.lstrip()
print greet
