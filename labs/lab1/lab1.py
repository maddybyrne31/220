"""
Name: <Madison Byrne>
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area= length * width
    print ("Area =",area)

calc_rec_area ()

def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume: length*width*height
    print ("Volume =", volume)

calc_volume()

def shooting_percentage():
    shots = eval(input("Enter the shots:"))
    total = eval(input("Enter the total:"))
    percentages = (shots/total)*100

shooting_percentage()

def coffee():
    x = eval(input("Enter the pounds:"))
    cost = 10.50
    shipping = 0.86
    fixed = 1.50
    coffee = ((cost*x)+(shipping*x)+fixed)
    print("Pounds =", x)
coffee()

def kilometers_to_miles():
    kilometers = eval(input("kilometers"))
    miles = kilometers/1.61





