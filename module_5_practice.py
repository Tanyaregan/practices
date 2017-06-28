# coding: utf-8
# counter = 1
# while counter < 8:
#     print counter
#     counter += 1

# counter = 1
# for num in range(20):
#     print num

# for num in range(1, 21):
#     print num

# for num in range(1, 11):
#     if num == 3:
#         continue
#     elif num == 8:
#         continue
#     else:
#         print num

# for num in range(1, 11):
#     if num == 3:
#         continue
#     elif num == 5:
#         continue
#     else:
#         print num

# index = 101
# while index > 1:m in range(1. 101):
# list = range(101, 1, -1)
# list
# list = range(100, 1, -1)
# list
# list = range(100, 0, -1)
# list
# index = 100
# while index < 1:
#     for num in list:
#         print num
#         index -= 1

# while index > 1:
#     for num in list:
#         print num
#         index -= 1

# while index > 1:
#     for num in list:
#         if num % 11 == 0:
#             print num
#             index -= 1

# index = 100
# while index > 1:
#     for num in list:
#         if num % 11 == 0:
#             print num
#             index -= 1

# while index > 1:
#     for num in list:
#         if num % 11 == 0:
#             print num
#             index -= 1
#         if index == 1:
#             break


# index = 100
# while index > 1:
#     for num in list:
#         if num % 11 == 0:
#             print num
#             index -= 1
#         if index == 1:
#             break


# for num in range(101, 1, -1):
#     if num % 11 == 0:
#         print num

# for num in range(80):
#     print num

# colors = ["black", "orange", "purple"]
# for color in colors:
#     print color

# for color in colors:
#     print color[0]

# for num in range(7, 13):
#     print num

# for num in range(8, 13):
#     if num % 2 == 0:
#         print num

# get_ipython().magic(u'save module_6_practice 1-32')

quiz_questions = ['what is a string?', 'what is an integer?', 'what is a Boolean?']
question_index = 0

for question in quiz_questions:
    print question
    answer = raw_input()

todo_list = []
todo_list.append('Laundry')
print 'To do list has items:', todo_list

command = raw_input('Would you like to add another chore to the list? (add to enter, quit to exit)')

while command != 'quit':
    if command == 'add':
        chore = raw_input('chore to add?: ')
        todo_list.append(chore)
    command = raw_input('Would you like to add another chore to the list? (add to enter, quit to exit)')

for chore in todo_list:
    print chore
