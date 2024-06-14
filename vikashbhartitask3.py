# TASSK 2 :-
# Design an INDIAN FLAG using python turtle
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=600, height=400)
screen.bgcolor("#FFFFFF")

# Create a turtle object
flag = turtle.Turtle()
flag.speed(2)

# Function to draw rectangle
def draw_rectangle(color, x, y, width, height):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

# Function to draw the Ashoka Chakra
def draw_chakra(color, x, y, radius):
    flag.penup()
    flag.goto(x, y - radius)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    flag.circle(radius)
    flag.end_fill()

# Draw green rectangle
draw_rectangle("#138808", -250, 150, 500, 100)

# Draw white rectangle
draw_rectangle("#FFFFFF", -250, 50, 500, 100)

# Draw saffron rectangle
draw_rectangle("#FF9933", -250, -50, 500, 100)

# Draw Ashoka Chakra
flag.pensize(3)
draw_chakra("#000080", 0, 50, 40)

# Hide the turtle
flag.hideturtle()

# Keep the window open
screen.mainloop()
