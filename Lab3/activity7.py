# Import Turtle graphics library
import turtle

# Set up your drawing parameters
ITERATIONS = 40 # The number of shapes to draw
ANGLE = 10 # The angle to rotate the turtle after each shape
SIZE = 50# The size parameter for the shapes

# Set up the Turtle screen and turtle
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()

# Loop to draw the pattern
for i in range(ITERATIONS):
    # Draw your geometric shape here
    # E.g., to draw a square:
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  # Right angle for a square

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLE)

turtle.left(90)
turtle.penup()
turtle.forward(200)
turtle.pendown()

for x in range(ITERATIONS):
   #draw octagon
    for y in range(8):
        turtle.color("blue")
        turtle.forward(SIZE)
        turtle.right(45)

pattern_turtle.right(ANGLE)
# Complete the program with a command to keep the window open
turtle.done()

