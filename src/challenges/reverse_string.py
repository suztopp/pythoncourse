word = input("Please enter a sentence after the colon: ")

length = len(word) - 1
backwards = ""

while length >= 0:
    backwards += word[length]
    length -= 1

print(backwards)

# their example
# for item in range(len(user_string) - 1, -1, -1):
#     reversed += user_string[item]



