# counter = 0
#
# while counter < 3:
#     print("something")
#     counter += 1
#
# new_counter = 10
#
# while new_counter >= 0:
#     print(new_counter)
#     new_counter -= 1

# new_number = int(input("Please enter an int of your choice: "))
# added = 0
#
# while new_number > 0:
#     added += new_number
#     new_number -= 1
#
# print("total = ", added)

# word = "house"
#
# for letter in word:
#     print(letter)
#
# range() start stop step

one_input = range(5)  # 0 1 2 3 4 stop

for num in one_input:
    print(num)

two_inputs = range(5, 10)  # 5 6 7 8 9 start stop

three_inputs = range(1, 20, 3)  # 1 4 7 10 13 16 19 start stop step

