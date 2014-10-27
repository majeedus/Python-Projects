## America
## 9/25/2012
## Usman M.

import turtle
import time
import random

def get_color(color2):
    ## If color2 equals 1, then make the color white.
    if color2 == 1:
        r = g = b = 1
        return (r, g, b)
    ## If color2 equals 1, then make the color red.
    if color2 == 0:
        r = 1
        g = 0
        b = 0
        return (r, g, b)
    ## If color2 equals 1, then make the color black.
    if color2 == 2:
        r = 0
        g = 0
        b = 1
        return (r, g, b)
    
def draw_rectangle(length, height, color):
    turtle.up()
    x = -150
    y = 150
    C = height*(7/13)
    D = length*(2/5)
    L = stripe_width = float(round(height/13,1))

    ## Draw main rectangle first.
    color2 = 0 ## Red flag background.
    color = get_color(color2)
    turtle.color(color)
    turtle.begin_fill()
    turtle.setpos(x,y)
    turtle.down()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()
    
    ## Then draw the stripes.
    x1 = -150
    y1 = 150-L
    ## Make sure that the color for the stripes alternate.
    for z in range(1,14):
        if z%2 == 0: ## If the number is even, its a white stripe.
            color2 = 1
            color = get_color(color2)
            turtle.up()
            turtle.speed(100)
            turtle.setpos(x1,y1)
            turtle.setheading(90)
            turtle.down()
            turtle.color(color)
            turtle.begin_fill()
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length)
            turtle.end_fill()
            y1 -= L
        else: ## If the number is odd, its a red stripe.
            color2 = 0
            color = get_color(color2)
            turtle.up()
            turtle.speed(100)
            turtle.setpos(x1,y1)
            turtle.setheading(90)
            turtle.down()
            turtle.color(color)
            turtle.begin_fill()
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length)
            turtle.end_fill()
            y1 -= L

    ## Finally draw the rectangle which contains the stars.
    color2 = 2
    color = get_color(color2)
    x2 = -150+D
    y2 = 150.5-C
    turtle.up()
    turtle.setpos(x2,y2)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.right(90)
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.end_fill()
    turtle.up()

    ## Now draw the stars.
    draw_star(-length, height, color)

def draw_star(l, h, color):
    ## This function and its respective if loops define the rows (5 total).
    for z in range(50):
        if z < 7:
            row = 140
            draw_starrows(row)
        if z < 14:
            row = row - 20
            draw_starrows(row)
        if z < 21:
            row = row - 20
            draw_starrows(row)
        if z < 28:
            row = row - 20
            draw_starrows(row)
        if z < 35:
            row = row - 20
            draw_starrows(row)
            ## This gets the turtle pen out of the way at the very end.
            turtle.up()
            turtle.setpos(-180,100)
            time.sleep(5)
        break

def draw_starrows(row):
    color2 = 1
    color = get_color(color2)
    x = -160
    y = 150
    ## This for loop draws 10 stars for each row above (5 total x 10 = 50).
    for z in range(10):
        x += 15
        turtle.up()
        turtle.color(color)
        turtle.speed(100)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.end_fill()

def draw_flag():
    A = 200
    height = int(A)
    color = (0,0,0)
    draw_rectangle(height*1.9, height, color)
    ##  Dimension notes for easy access.
    ##  length = height*1.9
    ##  C = height*(7/13)
    ##  D = length*(2/5)
    ##  E = F = union_height/10
    ##  G = H = union_length/12
    ##  stripe_width = height/13
    ##  diameter_star = stripe_width*(4/5)

draw_flag()
turtle.bye()


