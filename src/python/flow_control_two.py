gpa = float(input("What is your GPA currently: "))
accepted = True

if gpa >= 3.7:
    if accepted:
        print("You have qualified for the low APR loan")
    else:
        print("Your application does not qualify for the low APR loan")
else:
    print("Sorry you need to gain a higher gpa to qualify")
