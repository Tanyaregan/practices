# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return
# home after 10 nights.
# Write a general version of the program which asks for the starting day number,
# and the length of your stay, and it will tell you the number of day of the week
# you will return on.

print 'Sunday is day 0, Saturday is day 6.'
start_day = int(raw_input('What day are you leaving (1-6)?: '))
days_away = int(raw_input('How many days will you be gone?: '))
days_gone = (start_day + days_away)
return_day = days_gone % 7

if return_day == 0:
    return_day = 'Sunday'
elif return_day == 1:
    return_day = 'Monday'
elif return_day == 2:
    return_day = 'Tuesay'
elif return_day == 3:
    return_day = 'Wednesday'
elif return_day == 4:
    return_day = 'Thursday'
elif return_day == 5:
    return_day = 'Friday'
else:
    return_day = 'Saturday'

print 'You are returning on a', return_day, 'after being gone for', days_gone, 'days.'
