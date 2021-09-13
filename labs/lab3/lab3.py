"""
Name: <Madison Byrne>
<lab3>.py

Problem: Develop simple Python programs that do input, produce output and do arithmetic using loops

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def average():
   hw = eval(input("enter a grade for the homework"))
   acc = 0
   for i in range (hw):
        grade = eval(input("enter a value for homework:" + str(i+1)))
        acc = acc + grade
   print(acc/hw)


average()

def tip_jar():
    donation = eval(input("enter amount for the total amount of donation added in the jar:"))
    acc = 0
    for i in range (5):
        donation = eval(input("enter a value for the donation:" + str(i+1)))
        acc = acc + donation
    print(tip_jar)

tip_jar()

def sequence():
    x = eval(input("enter the number of terms in the series:"))
    for i in range (0,x+1):
        print(1 * (x // 2) * 2)

sequence()

def newton():
    x = eval(input("enter a value for x:"))
    refine = eval(input("enter the number of refine"))
    approx = x/2
    for i in range (refine):
        approx = (approx+(x/approx))/2
    print(approx)

newton()

def pi():
    x = eval(input("enter a value that approximates the value of pi"))
    acc = 1
    for i in range (1, x + 1):
        numerator = (2 + (i//2 * 2))
        denominator = 1 + ((i+1)//2 * 2)
        frac = numerator/denominator
        acc = acc * frac
        print (acc)

pi()

