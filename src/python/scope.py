example = "hello world"  # global


def loc_ex():
    example = "this is a string"  # local
    return example


print(example)
print(loc_ex())


def loc_ex():
    global fruit
    fruit = "pear"
    test = "test"
    print(fruit)


fruit = "apple"
loc_ex()
print(fruit)  # need to have the global fruit line in the loc ex function
# to be able to change the actual global variable

# print(test)


