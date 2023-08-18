# def my_function(param):
#     print(param + 2)
#
# my_function(8) # calling the function

# def my_function(p1, p2, p3):
#     print(p1 + p2 + p3)
#
# my_function(8, 6, 4) # calling the function

# def example(num1=7, num2=9):
#     print(num1 + num2)
#
#
# example(2, 6)  # these will substitute in for the defaults in this case

# need to use return to assign result of function to a variable

# def example(num1=7, num2=10):
#     return num1 * num2
#
#
# answer = example()
# print(answer)

# have to use the return statement for the following
# def example(num1=7, num2=10):
#     # print(num1 + num2)
#     return num1 + num2
#
#
# answer = example()  # won't work if the function doesn't return anything
# print(str(answer) + " answer")

# def hello_world_printer():
#     print("hello world")
#
# hello_world_printer()

# length = input("Please enter a length: ")
# width = input("Please enter a width: ")
# height = input("Please enter a height: ")
# # or could do height = int(input("Please enter a height: "))
#
#
# def volume(le, wi, he):
#     return le * wi * he
#
#
# print("The volume of the rectangular prism is: " + str(volume(int(length), int(width), int(height))))

temp = int(input("Please enter the temp in celsius: "))


def calc(c):
    # return 1.8 * c + 32
    # return (18 * c + 320) / 10
    return round((1.8 * c + 32), 1)


print("The Fahrenheit equivalent of " + str(temp) + " degrees Celsius is " + str(calc(temp)) + ".")







