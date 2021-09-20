"""
Name: Madison Byrne
<lab4>.py
Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move rectangle")
    instructions.draw(win)

        # create a space to instruct user
    inst_pt = Point(width / 2, 10)
    instructions = Text(inst_pt, "Click to move rectangle")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_click = win.getMouse()
        # builds a circle
        shape = Rectangle(Point(user_click.x - 10, user_click.y -10), Point(user_click.x +10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    pass
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4 Rectangles", width, height)
    Point_1 = win.getMouse()
    Point_2 = win.getMouse()

    rectangle = Rectangle(Point_1,Point_2)
    length = abs(Point_2.getX() - Point_1.getX())
    width = abs(Point_2.getY() - Point_1.getY())
    area = (length)*(width)
    perimeter = 2 * (length+width)

    txt = Text(Point(50, 50), "The area is: " + str(area))
    txt.draw(win)
    txt = Text(Point(50, 80), "The perimeter is: " + str(perimeter))
    txt.draw(win)

    rectangle.draw(win)

    win.getMouse()
    win.close()


def circle():


    win = GraphWin("Lab 4")
    P1 = win.getMouse()
    P2 = win.getMouse()
    X_one = P1.getX()
    X_two = P2.getX()
    Y_one = P1.getY()
    Y_two = P2.getY()
    r = math.sqrt ((X_two-X_one)**2 * (Y_two-Y_one) **2)
    circle= Circle(P1,r)
    circle.draw(win)

    win.getMouse()
    win.close()


def pi2():
    x = eval(input("enter a value that approximates the value of pi"))
    acc = 0
    for i in range(x):
        numerator = 4
        denominator = 1 + 2 * i
        fraction = (numerator/denominator)*((-1)**i)
        acc = (acc + fraction)
    print(acc)
    print(math.pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
