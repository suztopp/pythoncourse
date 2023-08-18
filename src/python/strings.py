example = "hello i'm suz"
print(example[2])
print(example[4].upper())
print("answer ", example[2:5]) # prints 2 3 4
print("answer ", example[3:]) # prints 3 to end
print("answer ", example[:4]) # prints 0 1 2 3

concatenated = "R2" + " - " + "D2"
print(concatenated)

string_word = "Just do it!"
print(string_word[-1])
print(string_word[5:7])
print(string_word[-3:])
print(string_word[:4])
print("Don't " + string_word[-6:])

word = "hello there"
print(type(word).__name__)
print(type(word))
int_test= 5
int_test_two = str(int_test)
print(int_test_two)
print(type(int_test_two))

print("this\tis\ta\tsentence")
print("this\nis\na\nsentence")
#to put quotes in your strings
print('"When I said \'immediately,\' I meant today!" said the King')

# escape sequences for backslashes in strings
print("all escape sequences contain a \\")

line_one = "*******"
line_two = " ***** "
line_three = "  ***  "
line_four = "   *   "
print(line_one + "\n" + line_two + "\n" + line_three + "\n" + line_four)



