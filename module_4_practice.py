# coding: utf-8
# languages = ['Portuguese', 'English', 'Spanish', 'Russian', 'Mandarin']
# print languages[2]
# print languages[0]
# print languages[-1]
# languages.append('French')
# languages
# print languages[-1]
# languages.pop()
# languages.sort()
# languages
# languages.insert('French', 1)
# languages.insert(1, 'French')
# languages
# my_nums = range(12)
# my_nums
# characters = ['Brienne', 'Sansa', 'Daenerys', 'Tyrion', 'Jaime', 'Cersei']
# furniture = ['chair', 'table', 'desk', 'lamp']
# odd_nums = [1, 3, 5, 7, 9, 11]
# even_nums = [0, 2, 4, 6, 8, 10]
# todo_list = ['finish the modules', 'start next headfirst python chapter']
# characters.append('Tormund')
# furniture.append('bed')
# odd_nums.append(13)
# even_nums.append(12)
# todo_list.append('cook dinner')
# listy = range(7)
# listy
# todo_list.pop()
# furniture.pop()
# odd_nums[2]
# even_nums[4]
# word1 = 'delicious'
# word1[4]
# word1 = 'yummy'
# word1[1]
# some_numbers = [4, 2, 1, 6, 8]
# some_numbers.sort()
# some_numbers
# get_ipython().magic(u'save module_4_practice 1-40')

# HOMEWORK

travel = raw_input('Where would you like to travel?: ')
travel2 = raw_input('Where else would you like to travel?: ')
travel3 = raw_input('One more place would you like to travel?: ')

destinations = []

destinations.append(travel)
destinations.append(travel2)
destinations.append(travel3)

destinations.sort()

print 'You said youd like to go to', destinations[0]
print 'You also said youd like to go to', destinations[1]
print 'You finally said youd like to go to', destinations[2]


fun_words = ["elephant", "balloon", "macchiato", "angostura"]

first_letters = []
third_letters = []

for word in fun_words:
    first_letters.append(word[0])

for word in fun_words:
    third_letters.append(word[2])

print first_letters
print third_letters

websites = ["facebook", "twitter", "buzzfeed"]
fruits = ["apple", "banana", "mango", "berry"]
names = ["Bob", "Alice", "Henry", "Rick", "Carl"]

len_web = len(websites)
len_fru = len(fruits)
len_name = len(names)

lengths = []

lengths.append(len_web)
lengths.append(len_fru)
lengths.append(len_name)

print 'Lengths =', lengths

list_of_25 = range(25)
print 'List of 25 numbers:', list_of_25

print list_of_25[0]
print list_of_25[4]
print list_of_25[9]
print list_of_25[14]


