"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    import math
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3= win.getMouse()

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    p1_x = p1.getX()
    p1_y = p2.getY()

    p2_x = p2.getX()
    p2_y = p2.getY()

    p3_x = p3.getX()
    p3_y = p3.getY()



    L1 = math.sqrt ((p2_x-p1_x)**2 + (p2_y-p1_y) **2)
    L2 = math.sqrt ((p3_x-p2_x)**2 + (p3_y-p2_y) **2)
    L3 = math.sqrt ((p3_x-p1_x)**2 + (p3_y-p1_y) **2)

    perimeter = (L1+L2+L3)
    s = perimeter / 2
    area = math.sqrt (s(s-L1) * (s-L2) * (s-L3))

    ptext = Text(Point, "The area is: " + str(area))
    ptext.draw(win)

    ptext = Text(Point, "The perimeter is: "+ str(perimeter))
    ptext.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", 400, 400)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_entry = Entry(Point(win_width / 2 , win_height / 2 + 40),5)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_entry = Entry(Point(win_width / 2 , win_height / 2 + 70),5)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_entry = Entry(Point(win_width / 2 , win_height / 2 + 100),5)
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry.draw(win)
    blue_entry.draw(win)
    green_entry.draw(win)

    # Wait for another click to exit
    win.getMouse()
    for i in range(5):
        blue = int(blue_entry.getText())
        red = int(red_entry.getText())
        green = int(green_entry.getText())
        color= color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()

    win.close()

def process_string():
    S = input("process string")
    print(S[0])
    print(S[-1])
    print(S[2:6])
    print(S[0]+S[-1])
    print(S[0:3]*10)
    for c in S():
        print(c)
    print(len(S))


def value():
    values = eval(input("Enter a variable for your values: "))
    x = values[2] + values[4]
    print(x)
    x = values [1] + values [3]
    print(x)
    x =[values[5]*5]
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = value[0] + value [2] + value [5]
    print(x)
    print(len(x))

def another_series():
    n = eval(input("enter a value for your terms"))
    acc = 0
    for i in range(n):
        y = 2+(2 * n % 3)
        print(y, end = "")
        acc += y
    print("sum=", acc)


def main():
    # triangle()
    # color_shape()
    pass


main()
