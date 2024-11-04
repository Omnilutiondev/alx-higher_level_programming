#!/usr/bin/python3
def fizzbuzz():
    for idx in range(1, 99):
        if idx % 15 == 0:
            print("FizzBuzz", end=" ")
        elif idx % 5 == 0:
            print("Buzz", end=" ")
        if idx % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(idx), end=" ")
