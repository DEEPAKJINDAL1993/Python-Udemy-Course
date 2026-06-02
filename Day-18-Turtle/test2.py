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

# Function to draw a spiral design
def draw_spiral():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)  # Face the turtle to the right

    for i in range(300):  # Increase the number for a larger spiral
        t.color(random.choice(colors))  # Pick a random color
        t.forward(i * 2)  # Move forward with increasing steps
        t.right(61)  # Slightly change the angle for a nice spiral effect

# Draw the colorful spiral
draw_spiral()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
