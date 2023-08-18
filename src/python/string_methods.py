# string = "Hello There"
#
# print(string.upper())
# print(string.lower())
#
# print(string.isupper())
# print(string.islower())
#
# title = "the great gatsby"
#
# print(title.title())
#
# string_word = "This is a string"
#
# print(string_word.startswith("this"))  # false
# print(string_word.endswith("string"))  # true
#
# print(string.join(string_word))  # returns weird stuff
#
# print(" , ".join([string, string_word]))
#
# print(string_word.split())
#
# print("Eggs, Milk, Waffles, Bacon".split(", "))
#
# mixed_case = "A Song of Ice and Fire"
# print(mixed_case.isupper())
# print(mixed_case.islower())
# print(mixed_case.upper())
# print(mixed_case.lower())
# print(mixed_case.istitle())
# title_case = mixed_case.title()
# print(title_case)
# print(mixed_case.startswith("e"))
# print(mixed_case.endswith("e"))
# words = mixed_case.split(" ")
# print(words)
# print(" ".join(words))

word_one = "hello world"
print(word_one.rjust(15))  # total length of string returned by adding spaces to the right side
print(word_one.ljust(15))  # opposite
print(word_one.rjust(15, "*"))  # fill characters

print(word_one.center(15, "*"))

word_two = "*      hello there        *"
print(word_two)
print(word_two.rstrip(" *"))
print(word_two.lstrip("* "))

print("good morning".replace("morning", "evening"))

sentence = "hello there how are you"
print(sentence.lstrip("hello "))
print(sentence.rstrip(" you"))

# length
print(len(sentence))

# FORMAT

name = "Suzanne"
work = "Engineer"
experience = 2
degree = "Diploma of IT"

print("{} majored in a {}, works as a {}, and has {} years of experience".format(name, degree, work, experience))




