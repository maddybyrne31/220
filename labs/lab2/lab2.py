"""
Name: <Madison Byrne>
<Arithmetic>.py

Problem: Develop simple Python programs that do input, produce output and do arithmetic

"""
import math


def sum_of_threes():
    a = eval(input("Enter an upper bound: "))
    acc = 0
    for x in range (0, a, 3):
        acc= acc + x
    print(acc)

sum_of_threes()

def multiplication_table():
    for h in range (1, 11):
        for L in range (1, 11):
            print(h * L, end =" ")
        print()

multiplication_table()

def triangle_area():
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval (input("Enter the length of side c: "))
    z = (a + b + c)/ 2
    area = math.sqrt(z*(z-a)*(z-b)*(z-c))
    print(area)

triangle_area()

def sumSquares():
    a = eval(input("Enter the upper range: "))
    b = eval(input("Enter the lower range: "))
    acc = 0
    for x in range(0, a+1):
        acc = acc + (x * x)
    print(acc)

sumSquares()

def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print (acc)

power()
