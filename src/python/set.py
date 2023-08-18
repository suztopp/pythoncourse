set_1 = {8, 8, 7, 6, 8, 6}
set_2 = set({"a", "b", "c", "d"})  # not suggested by pycharm

print(set_1)
print(set_2)

# duplicates are ignored, like a hash set in java

set_3 = set(range(1, 12, 2))  # 1 3 5 7 9 11

print(set_3)

#sets can hold different data types

set_4 = {"hello", True, 7, 9}

for value in set_4:
    print(value)

# In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.

print(9 in set_4)  # True

scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)

scifi.remove("star trek")
print(scifi)

# scifi.clear()
# print(scifi)  # set()

scifi_2 = scifi.copy()

print(scifi_2 is scifi)  # False as not same set

set_5 = {1, 2, 3}
set_6 = {4, 5, 6}
set_7 = set_5.union(set_6)
print(set_7)
# could also do set_7 = set_5 | set_6

set_8 = set_5.intersection(set_7)
print(set_8)  # only prints the numbers that appear in each 1 2 3
# can also use the ampersand here set_5 & set_7

set_9 = set_6 - set_7
set_10 = set_1.difference(set_7)
print(set_9)

# could also do set_7 = set_5 | set_6

# set comprehensions

comp_1 = {even+2 for even in range(2, 11, 2)}
# action done to each item, for loop deciding what to loop over, range that is set
# starting at 2, for all even numbers add 2 and put into comp_1

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)

dir()

# pep8 compliance
# mypy
# linter









