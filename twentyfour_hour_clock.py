# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours), and then ask for the number of hours to wait
# for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.


now_time = int(raw_input('What is the current time (in hours)?: '))
alarm_delay = int(raw_input('How many hours from now should the alarm go off?: '))
alarm_set = now_time + alarm_delay
alarm_time = alarm_set % 24


print 'The current time is:', now_time
print 'In', alarm_delay, 'hours, your alarm will sound. it will be', alarm_time, '.'
