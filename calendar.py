# This is a calendar program that views, adds, updates and deletes events.

from time import strftime

USERNAME = 'Tanya'
calendar = {}


def welcome():
    """Welcomes user."""

    print 'Welcome ' + USERNAME
    print "Calendar is opening.."
    print strftime('%A %B %d, %Y')
    print strftime('%H:%M:%S')
    print 'What would you like to do?: '


def start_calendar():
    """Runs calendar code."""
    welcome()

    start = True
    while start is True:
        user_choice = raw_input('A to Add, U to Update, V to View, D to Delete, X to Exit: ')
        user_choice = user_choice.upper()
        print user_choice

        if user_choice == 'V':
                if len(calendar.keys()) == 0:
                    print 'Your calendar is empty, nothing to view'
                else:
                    print calendar

        elif user_choice == 'U':
                date = raw_input('What date?: ')
                update = raw_input('Enter the update: ')
                calendar[date] = update
                print 'Update succesful!'
                print calendar

        elif user_choice == 'A':
                event = raw_input('Enter event: ')
                date = raw_input('Enter date (MM/DD/YYYY): ')
                if len(date) != 10 or int(date[6:]) < int(strftime('%Y')):
                    print 'Sorry, that date was invalid.'
                    try_again = raw_input('Try Again? Y for Yes, N for No: ')
                    try_again = try_again.upper()
                    if try_again == 'Y':
                        continue
                    else:
                        start = False
                else:
                    calendar[date] = event
                    print calendar

        elif user_choice == 'D':
                if len(calendar.keys()) == 0:
                    print 'Your calendar is empty, nothing to delete.'
                else:
                    event = raw_input('Enter event: ')
                    for date in calendar.keys():
                        if calendar[date] == event:
                            del calendar[date]
                            print 'Event was deleted.'
                            print calendar
                        else:
                            print 'Sorry, there was no event by that name.'

        elif user_choice == 'X':
            start = False

        else:
            print 'Sorry, that command was invalid'
            start = False

start_calendar()

