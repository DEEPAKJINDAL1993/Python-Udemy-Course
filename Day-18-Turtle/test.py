import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Background color

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)  # Set the pen width

# List of vivid colors
colors = ["#FF5733", "#33FF57", "#3357FF", "#F7FF33", "#FF33F6", "#33FFF6", "#FF3333"]

# Function to draw a polygon with n sides
def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Function to draw a pattern with concentric polygons
def draw_pattern():
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(50):
        t.color(random.choice(colors))  # Choose a random color from the list
        draw_polygon(6, i * 10 + 50)   # Draw a polygon (hexagon)
        t.right(10)                    # Rotate the polygon slightly to create a pattern

# Function to draw a starburst design
def draw_starburst():
    t.penup()
    t.goto(0, -100)
    t.pendown()

    for i in range(36):
        t.color(random.choice(colors))
        t.forward(200)
        t.backward(200)
        t.right(10)

# Draw the pattern
draw_pattern()

# Move the turtle to a new position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the starburst design
draw_starburst()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
