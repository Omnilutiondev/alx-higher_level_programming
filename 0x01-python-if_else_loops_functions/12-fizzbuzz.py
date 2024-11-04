#!/usr/bin/python3
def fizzbuzz():
    for b in range(1, 100):
        if b % 15 == 0:
            print("FizzBuzz", end=" ")
        elif b % 5 == 0:
            print("Buzz", end=" ")
        if b % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(b), end=" ")
