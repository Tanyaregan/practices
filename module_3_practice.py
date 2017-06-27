# # coding: utf-8
# adjective = 'Absolutely fabulous'
# adjective2 = 'supercalifragilistic'
# noun = 'aardvarks'
# noun2 = 'goats'
# verb = 'lollygagging'
# verb2 = 'jogging'
# if len(adjective) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# if len(adjective2) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# if len(noun) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# if len(noun2) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# if len(verb) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# if len(verb2) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# something = raw_input('Type a thing ")
# something = raw_input('Type a thing ')
# if len(something) > 9:
#     print 'That is a long string.'
# else:
#     print 'Not so long.'

# answer = raw_input('What is 2 + 2? ')
# answer_as_integer = int(answer)
# answer = int(raw_input('What is 2+2 ? '))
# if answer == 4:
#     print 'correct!'
# elif answer > 4:
#     print 'Too high'
# else:
#     print 'Too low'

# answer = int(raw_input('What is 2+2 ? '))
# if answer == 4:
#     print 'correct!'
# elif answer > 4:
#     print 'Too high'
# else:
#     print 'Too low'

# answer = int(raw_input('What is 2+2 ? '))
# if answer == 4:
#     print 'correct!'
# elif answer > 4:
#     print 'Too high'
# else:
#     print 'Too low'

# if verb == verb2:
#     print 'they are the same'
# else:
#     print 'verb is:', verb, 'verb2 is:', verb2, '. These are not the same.'

# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating-as_integer > 7:
#     'You love it, there is no place like home.'
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating-as_integer > 7:
#     'You love it, there is no place like home.'
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating-as_integer > 7:
#     'You love it, there is no place like home.'
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating_as_integer > 7:
#     'You love it, there is no place like home.'
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating_as_integer > 7:
#     print 'You love it, there is no place like home.'
# 3
# 3
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating_as_integer > 7:
#     print 'You love it, there is no place like home.'
# rating = raw_input('On a scale of 1-10, how would you rate the Wizard of Oz? ')
# rating_as_integer = int(rating)
# if rating_as_integer < 5:
#     print 'Wow, you hated it!'
# elif rating_as_integer < 7:
#     print 'You are meh about this movie.'
# elif rating_as_integer > 7:
#     print 'You love it, there is no place like home.'
# get_ipython().magic(u'save module_3_practice 1-35')


# Homework

cats = raw_input('Do you like cats? Answer Y or N ')
if cats == 'Y':
    print 'Cats are lovely.'
elif cats == 'N':
    print 'What is your favorite animal? '
    fave_animal = raw_input('')
    print fave_animal, 'is pretty good too'


dessert = raw_input('Do you like chocolate? Answer Y or N: ')
if dessert == 'Y':
    print "Chocolate is tasty"
else:
    fave_dessert = raw_input('WHat is your favorite dessert? ')
    print fave_dessert, 'is also yummy'


coffee = raw_input('Do you drink coffee? Answer Y or N: ')
if coffee == 'Y':
    sugar = raw_input('Do you put sugar in it? Y or N: ')
    if sugar == 'Y':
        print 'sweet tooth ftw!'
    else:
        print 'coffee is better with sugar.'
else:
    fave_drink = raw_input('What is your favorite drink ?: ')
    print fave_drink, 'is good too.'


native = raw_input('Do you live in California? Y or N: ')
if native == 'Y':
    ca_city = raw_input('What California city do you live in? ')
    print ca_city, 'is wonderful.'
else:
    state = raw_input('What state do you live in? ')
    print state, 'is ok too.'

joker = raw_input('Do you enjoy jokes? Answer Y or N ')
if joker == 'Y':
    print 'What kind of melons cant marry?'
    answer = raw_input()
    print "Cantelopes!"
else:
    party_pooper = raw_input('Why dont you like jokes, loser? ')
    print party_pooper, 'is a bad reason not to like jokes.'
