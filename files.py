data = open('data.txt')

# num_lines = 0
# for line in data:
#     num_lines += 1
# print 'There are', num_lines, 'lines of info in this file'

# all_items = data.read()
# print all_items
# print 'There are', len(all_items), 'total characters in the file'

# add_lines = 0
# for line in data:
#     if line.startswith('Add'):
#         add_lines += 1
#         print line.rstrip()
# print 'There are', add_lines, 'lines that start with the word add'

# add_lines = 0
# for line in data:
#     line = line.rstrip()
#     if not line.startswith('Add'):
#         continue
#     else:
#         add_lines += 1
#         print line
# print 'There are', add_lines, 'lines that start with the word add'

# lemon_lines = 0
# for line in data:
#     line = line.rstrip()
#     if not 'lemon' in line:
#         continue
#     else:
#         lemon_lines += 1
#         print line
# print 'There are', lemon_lines, 'lines that have the word lemon in them'

# file_name = raw_input('What is the file name?: ')
# try:
#     info = open(file_name)
# except:
#     print 'That aint no file name!'
#     exit()
# stir_count = 0
# for line in info:
#     if 'stir' in line:
#         stir_count += 1
#         print line
# print 'there are', stir_count, 'lines with the word stir in them'

# file_name = raw_input("Enter file name: ")
# open_file = open(file_name)
# string = open_file.read()
# string.rstrip()
# print string.upper()

file_handle = open('mbox.txt')
lines = 0
total = 0

for line in file_handle:
    if line.startswith("X-DSPAM-Confidence: "):
        lines += 1
        num_start = len("X-DSPAM-Confidence: ")
        num = line[num_start:]
        total += float(num)

spam_av = total / float(lines)

print 'Average spam confidence:', spam_av


