def kitchen_companion():
    """Displays and edits a list of ingredients."""

    import random

    print 'Welcome to Kitchen Companion!'

    ingredient_list = []
    ingredients = open('ingredients.txt', 'r+')
    for i in ingredients:
        ingredient_list.append(i.rstrip())

    while True:

        print ''
        print '*** INGREDIENTS LIST MAIN MENU ***'
        print ''
        print 'Would you like to:'
        print ''
        print '(L) List your ingredients in alphabetical order'
        print '(A) Add an ingredient'
        print '(R) Remove an ingredient'
        print '(S) Search for a specific ingredient'
        print '(X) Pick a random ingredient'
        print '(Q) to quit.'

        choice = raw_input('>>> ')

        if choice == 'L':
            print ''
            print 'Your ingredients:'
            for item in sorted(ingredient_list):
                print item
            continue

        elif choice == 'A':
            print ''
            print 'What ingredient would you like to add?: '
            addition = raw_input('>>> ')

            if addition not in ingredient_list:
                ingredient_list.append(addition)
                print addition, 'has been added to the list.'
                continue
            else:
                print addition, 'is already on the list.'
                continue

        elif choice == 'R':
            print ''
            print 'What ingredient would you like to delete?: '
            deletion = raw_input('>>> ')

            if deletion not in ingredient_list:
                print deletion, 'is not on the list'
                continue
            else:
                ingredient_list.remove(deletion)
                print deletion, 'removed from list'
                continue

        elif choice == 'S':
            print ''
            print 'What item would you like to search for?: '
            search = raw_input('>>> ')

            for item in ingredient_list:
                if item.startswith(search):
                    print item
                    continue

        elif choice == 'X':
            print ''
            print 'Here is a random item, you silly Balloonicorn:'
            rand = random.choice(ingredient_list)
            print rand

        elif choice == 'Q':
            print ''
            print 'Thanks for using Kitchen Companion!'
            break

        else:
            print 'That entry is not in the list of choices, please try again.'
            continue

    ingredients.close()

kitchen_companion()
