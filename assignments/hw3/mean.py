
"""
Name: <Madison Byrne>
<mean>.py

Problem: create a program that represents three different ways of calculating mean

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def mean():
    n = eval(input("Number of terms you have: "))
    total = 0
    for n in range(n):
        values = eval(input("Enter the values of your numbers:"))
        total = total + values

    arithmetic = total / n
    print("The arithmetic mean of a set of numbers", arithmetic)

