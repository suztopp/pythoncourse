range_nums = range(1, 51)

for num in range_nums:
    if num % 5 == 0 and num % 3 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("fizz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)



# if divisible by 3 print fizz
# if divisible by 5 print fizz
# if divisible by both print fizzbuzz
# else print numb




