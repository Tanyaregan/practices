def shopping1():
    """Displays and edits a list."""

    print 'Welcome to Shopping List 1.0!'
    shopping_list = []

    while True:

        print ''
        print '*** MAIN MENU ***'
        print 'Would you like to:'
        print '(1) Display your shopping list'
        print '(2) Add to your shopping list'
        print '(3) Delete from your shopping list'
        print '(4) Edit an item on your shopping list'
        print 'or enter Q to quit.'

        choice = raw_input('>>> ')

        if choice == '1':
            if shopping_list == []:
                print 'There\'s nothing on your list yet.'
                continue
            else:
                print 'Your shopping list: '
                for item in shopping_list:
                    print item
                continue

        elif choice == '2':
            entry = raw_input('Enter the item you would like to add: ')
            shopping_list.append(entry)
            print 'Item added!'
            continue

        elif choice == '3':
            entry = raw_input('What would you like to delete?: ')
            if entry not in shopping_list:
                print 'That item is not on your list.'
                continue
            else:
                shopping_list.remove(entry)
                print item, 'has been removed from your list.'
                continue

        elif choice == '4':
            entry = raw_input('What item would you like to edit?: ')
            if entry in shopping_list:
                edit = raw_input('What would you like to change it to?: ')
                shopping_list[shopping_list.index(entry)] = edit
                print entry, 'changed to', edit
                continue
            else:
                print 'That item is not on your list.'
                continue

        elif choice == 'Q':
            print 'Thanks for using Shopping List 1.0!'
            break

        else:
            print 'That entry is not in the list of choices, please try again.'
            continue


def shopping2():
    """Displays and edits a dictionary."""

    print 'Welcome to Shopping List 2.0!'

    shopping_list = {}

    while True:

        print ''
        print '*** MAIN MENU ***'
        print 'Would you like to:'
        print '(1) Display your stores and shopping lists'
        print '(2) Look up specific shopping list by store'
        print '(3) Add, edit or delete a store'
        print '(4) Add, edit or delete item from a shopping list'
        print 'or enter Q to quit.'

        choice = raw_input('>>> ')

        if choice == '1':
            if shopping_list == {}:
                print 'There\'s nothing here yet.'
                continue
            else:
                print 'Your lists:'
                for item in shopping_list:
                    print item, ':', shopping_list[item]
                continue

        elif choice == '2':
            if shopping_list == {}:
                print 'There\'s nothing here yet.'
                continue

            entry = raw_input('What store list would you like to view?: ')
            if entry not in shopping_list:
                print 'That store is not in your list.'
                continue
            else:
                print 'store:', entry
                print 'list:', shopping_list[entry]
                continue

        elif choice == '3':

            print 'Would you like to: (1) Add (2) Delete or (3) Edit?'
            print '(Q to exit to main menu):'
            entry = raw_input('>>> ')

            if entry == '1':
                store = raw_input('What store would you like to add?: ')
                shopping_list[store] = []
                print store, 'added!'
                continue

            elif entry == '2':
                store = raw_input('Which store would you like to delete?: ')
                if store not in shopping_list:
                    print 'That store is not on the list'
                    continue
                del shopping_list[store]
                print store, 'and the associated list have been removed'
                continue

            elif entry == '3':
                store = raw_input('Which store would you like to edit?: ')
                if store not in shopping_list:
                    print 'That store is not on the list'
                    continue
                edit = raw_input('What would you like to change it to?: ')
                shopping_list[edit] = shopping_list[store]
                del shopping_list[store]
                print store, 'has been changed to', edit
                continue

            elif entry == 'Q':
                break

            else:
                print 'That was not a valid option, please choose again.'
                continue

        elif choice == '4':
            store = raw_input('Which store list would you like to work with?: ')
            if store not in shopping_list:
                print 'That store is not on the list'
                continue

            print 'Would you like to: (1) Add (2) Delete or (3) Edit the list?'
            print '(Q to exit to main menu):'
            entry = raw_input('>>> ')

            if entry == '1':
                item = raw_input('What item would you like to add?: ')
                (shopping_list[store]).append(item)
                print item, 'added to', store, 'list.'
                print 'List is now: '
                continue

            elif entry == '2':
                item = raw_input('What item would you like to delete?: ')
                if item not in shopping_list[store]:
                    print 'Sorry, that store is not in the list.'
                    continue
                else:
                    shopping_list[store].remove(item)
                    print item, 'has been removed from', store, 'list.'
                    print 'List is now: '
                    print shopping_list[store]
                    continue

            elif entry == '3':
                item = raw_input('What item would you like to edit?: ')
                if item not in shopping_list[store]:
                    print 'Sorry, that item is not in the list.'
                    continue
                else:
                    edit = raw_input('What would you like to change it to?: ')
                    shopping_list[store][(shopping_list[store]).index(item)] = edit
                    print item, 'has been changed to', edit
                    print 'List is now: '
                    print shopping_list[store]
                    continue

            elif entry == 'Q':
                break

            else:
                    print 'That was not a valid option, please choose again.'
                    continue

        elif choice == 'Q':
            print 'Thanks for using Shopping List 2.0!'
            break

        else:
            print 'That entry is not in the list of choices, please try again.'
            continue

shopping2()
