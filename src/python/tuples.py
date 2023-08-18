tuple_1 = ("a", "b", "c")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = tuple("abcdef")

print(tuple_1)
print(tuple_2)
print(tuple_3)

print(tuple_1[0])
print(tuple_1[:2])

# tuples are for data that will not be changed
# days of the week, alphabet etc etc

tuple_4 = (1, 3, 5)
list_1 = [1, 3, 5]
print(tuple_4.__sizeof__())
print(list_1.__sizeof__())

count = 0
while count < len(tuple_4):
    print(tuple_4[count])
    count += 1

print(tuple_4[::2])  # from 0 to end steps of 2
print(tuple_3[4::1])  # one step starting at index 4

nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(nested[0])
print(nested[0][1])








