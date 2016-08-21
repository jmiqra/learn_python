import re

# Your code goes here
lists = []
for list in dir(re):
    if "find" in list:
        lists.append(list)

print sorted(lists)