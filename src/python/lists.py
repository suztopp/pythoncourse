import copy

example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = ["one", "two", "three"]
example_list_3 = [True, False, True, False]

print(list("blah"))  # 'b', 'l', 'a', 'h'

checked_list = [1, 2, 3, 4]
print(1 in checked_list)  # True

print(6 in checked_list)  # False

not_in = 8 not in checked_list  # True

bools = [1, 2.3, True]

answer = list("dogs")

print("e" in answer)

print("e" not in answer)

nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[0][2])

print(bools[-1])

print(answer[2:])
print(answer[:2])

answer[-1] = ("e")
print(answer)

# del answer[-1]
answer.remove("e")  # can select the item to remove from the list if it exists
print(answer)

answer.append("e")  # appends to end
print(answer)

answer.insert(-1, "u")
print(answer)

num_list = [3, 6, 10, 2, 7]
num_list.sort()
print(num_list)

word_list = ["dog", "cat", "marshy", "lara"]
word_list.sort()
print(word_list)
word_list.sort(reverse=True)
print(word_list)

# sort method uses ASCIIbetical order - upper case letters come before lower case letters
# False in a list would count as 0
# Capitalized words would come before ALL lower case words regardless of sorting

ascii = ["banana", "Brian", "cat", "Cow"]
ascii.sort()
print(ascii)  # ['Brian', 'Cow', 'banana', 'cat']
ascii.sort(key=str.lower)
print(ascii)  # ['banana', 'Brian', 'cat', 'Cow']

print(ascii.index("banana"))  # prints 0

ascii.pop(-1)
print(ascii)

# lists vs strings
# lists mutable, strings immutable

ex_1 = [1, 2, 3]
ex_1[1] = 4
print(ex_1)

string_word = "string"
# string_word[2] = "e"
# can't do this will error
print(string_word)

# create new strings from  old strings using concatenation etc

ex_3 = "no you can not"
ex_4 = "yes " + ex_3[3:10] + "!"
print(ex_4)

# reflection - create one list, copy it to another list
# change an index in the second list value wise
# will update the first list and second list

# copy() and deepcopy()
# deepcopy means it creates a new reference

ex_12 = [1, 2, 3, 4]
ex_13 = copy.deepcopy(ex_12)
ex_13[2] = 6
print(ex_12)
print(ex_13)

ex_15 = ["dog",
         "cat",
         "moth"]  # keep in line vertically

print(ex_15)

ex_16 = 2 + \
        4 + \
        6

print(ex_16)

ex_18 = "hello " + \
        "world"

print(ex_18)


