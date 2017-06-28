# coding: utf-8
# word_len = {}
# phrase = 'There once was a gal from nantucket'
# phrase_words = phrase.split()
# for word in phrase_words:
#     word_len[word] = len(word)

# print word_len
# word_len = {}
# for word in phrase_words:
#     word_len[len(word)] = word

# word_len
# word_len = {}
# for word in phrase_words:
#     num_chars = len(word)
#     if num_chars not in word_len:
#         word_len[num_chars] = []
#     word_len[num_chars].append(word)

# print word_len
# soccer_team = {}
# soccer_team['team_name'] = 'Losers'
# soccer_team['team_ranking'] = 4
# soccer_team['player_names'] = ['bob', 'joe', 'ed']
# soccer_team[team_rating] = soccer_team[team_rating] += 1
# soccer_team[team_rating] = soccer_team[team_rating] + 1
# soccer_team[team_ranking] = soccer_team[team_ranking] + 1
# soccer_team['team_ranking'] = soccer_team['team_ranking'] + 1
# soccer_team['team_ranking']
# soccer_team['team_names'].append('David Beckham')
# soccer_team['player_names'].append('David Beckham')
# soccer_team['player_names']
# if soccer_team['team_ranking'] > 3"
# if soccer_team['team_ranking'] > 3:
#     print "hooray!'
# if soccer_team['team_ranking'] > 3:
#     print "hooray!"
# else:
#     print 'You suck'

# for name in soccer_team['player_name']:
#     print name

# for name in soccer_team['player_names']:
#     print name


# if 'team_color' in soccer_team:
#     print 'team color is', team_color
# else:
#     print 'team is colorless'

# soccer_team['team_color'] = blue
# soccer_team['team_color'] = 'blue'
# if 'team_color' in soccer_team:
#     print 'team color is', team_color
# else:
#     print 'team is colorless'

# if 'team_color' in soccer_team:
#     print 'team color is',soccer_team['team_color']
# else:
#     print 'team is colorless'

# for stat in soccer_team:
#     print stat

# for key, value in soccer_team:
#     print key, value

# for stat in soccer_team:
#     print stat
#     print soccer_team[stat]

# get_ipython().magic(u'save module_6_practice 1-37')

# HOMEWORK
cake_ingredients = {}

cake_ingredients['butter'] = 1
cake_ingredients['shortening'] = .5
cake_ingredients['sugar'] = 3
cake_ingredients['egg_substitute'] = 1.5
cake_ingredients['flour'] = 3
cake_ingredients['milk'] = 1
cake_ingredients['salt'] = .01
cake_ingredients['baking_powder'] = .01

print 'To make 2 cakes, you need:'
for ingredient in cake_ingredients:
    print ingredient, cake_ingredients[ingredient] * 2

new_ingredient = raw_input('What would you like to add to this cake?: ')

if new_ingredient in cake_ingredients:
    print 'One cake has', cake_ingredients[new_ingredient], 'cups of', new_ingredient
else:
    print 'That ingredient isnt in the recipe'

