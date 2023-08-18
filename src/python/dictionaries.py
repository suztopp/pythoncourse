consoles = {"nintendo": "wii", "microsoft": "xbox"}

print(consoles["nintendo"])

print(consoles)

value = consoles["microsoft"]
print(value)

mixed = {"string": "hello", bool: True, float: 2.34}

print(mixed[bool])

print("string" in mixed)  # will print true that it does exist in the dictionary

print("string" not in mixed)  # will return false as the key exists

print(mixed.keys())  # returns dict_keys(['string', <class 'bool'>, <class 'float'>])

# you can loop through the keys of a dict

for key in mixed:
    print(key)  # prints each key on a new line

print(mixed.values())  # dict_values(['hello', True, 2.34])

# tuple - immutable, in () instead of []

for key, value in mixed.items():
    print(key, value)

print(list(mixed.values()))

print("hello" in mixed.values())  # returns true

print(mixed.get("string"))  # returns "hello"

if "word" in mixed:
    print(mixed["word"])
else:
    print("string is not a key in mixed")

print(mixed.get("word", "string word is not found in mixed"))

print(len(mixed))  # 3

music_list = {"Queen": "Bohemian Rhapsody",
              "Bee Gees": "Stayin' Alive",
              "U2": "One",
              "Michael Jackson": "Billie Jean",
              "The Beatles": "Hey Jude",
              "Bob Dylan": "Like A Rolling Stone"}

print(len(music_list))

for key in music_list.keys():
    print(key)

for value in music_list.values():
    print(value)

for key, value in music_list.items():
    print(key, value)

print(music_list.get("Promise of the Real", "Song not found"))

example_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
print(example_1)  # {'address': '1600 Pennsylvania Avenue NW'}

# if you didn't use a list of a string for the key, and used "address" alone
#     it would use each character as the keys
# ie. a, d, r, e, s

example_2 = {}.fromkeys(["address"])
print(example_2)  # {'address': None}

print(music_list.pop("U2"))
print(music_list)

# .popitem() removes a random key value pair

new_dict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for key, value in new_dict.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}

fast_food_items.popitem()
print(fast_food_items)

fast_food_items.clear()  # removes all items in dictionary
print(fast_food_items)

fast_food_items_2 = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
fast_food_items_3 = fast_food_items_2.copy()  # creates new dict with new reference
fast_food_items_3.popitem()
print(fast_food_items_2)
print(fast_food_items_3)

burger = {"Carls Jnr": "Veggie Burger"}
fast_food_items_3.update(burger)  # adds new item to the end of dictionary
print(fast_food_items_3)
print(fast_food_items_2)  # not changed at all

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
print(internet_celebrities)
another_another_one = another_one.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(another_another_one)

computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

# if "Lenovo" not in computers:
#     computers["Lenovo"] = "ThinkPad"
#
# print(computers)

computers.setdefault("Lenovo", "ThinkPad")  # does the same as above

print(computers)

computers.setdefault("Lenovo", "ThoughtPad")  # won't do anything
print(computers)

# dict()
empty = dict()
print(empty)  # returns an empty dictionary

with_values = dict(a1=1, b_=2, c_3=3)  # no spaces here
print(with_values)
# dict function call can only be characters underscores or numbers
# no special characters or punctuation










