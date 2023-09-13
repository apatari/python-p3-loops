#!/usr/bin/env python3

def happy_new_year():
    n = 10
    while n>0 :
        print(n)
        if n ==1 :
            print("Happy New Year!")
        n -= 1

def square_integers(int_list):
    res = [int * int for int in int_list]
    return res

def fizzbuzz():
    def fizzer(n):
        if  n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)
    for i in range(1, 101):
        fizzer(i)
