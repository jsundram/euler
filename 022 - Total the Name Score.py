# Using "022 - Total the Name Score.txt", a 46K text file containing over 5000
# first names,
# 1) Sort it into alphabetical order.
# Then, working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.
#
# e.g. When the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

filename = "022 - Total the Name Score.txt"
FILE = open(filename, "r")
contents = FILE.read()

# file looks like: "MARY","PATRICIA", etc.
names = contents.strip("\"").lower().split("\",\"")
names.sort()

base = ord('a') - 1
total = 0
for i, name in enumerate(names):
    score = 0
    for ch in name:
        score += (ord(ch) - base)
    total += (i+1) * score

print total

