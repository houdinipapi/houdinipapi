#!/usr/bin/python3

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
    if (num > 30):
        print("Number is greater than 30!!")
    else:
        print("Number is less than 30!!")
else:
    print("Odd Number")
    if (num > 30):
        print("Number is greater than 30!!")
    else:
        print("Number is less than 30!!")

print("Bye!!")
