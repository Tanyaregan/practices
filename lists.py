def averaging():
    """Takes a list of user input numbers and returns the average of them."""

    nums = 0
    total = 0

    while True:
        value = raw_input('Gimme a number: ')

        if value == 'quit':
            break

        try:
            dig = int(value)
        except:
            print 'That is not a number, dude'
            continue

        total = total + dig
        nums += 1

    ave = float(total / nums)

    print total
    print nums

    print 'the average of your numbers is', ave

# averaging()

# total = []

# while True:
#     value = raw_input('Gimme a number: ')
#     if value == 'quit':
#         break

#     try:
#         num = float(value)
#     except:
#         print 'That is not a number, jackass.'
#         continue

#     total.append(num)

# average = sum(total) / len(total)

# print 'average of your numbers is', average


#

fh = open('mbox.txt')
count = 0

for line in fh:
    if line.startswith("From "):
        count += 1
        splitsky = line.split()
        print splitsky[1]


print "There were", count, "lines in the file with From as the first word"
