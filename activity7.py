import turtle
import tkinter.simpledialog as simpledialog
# Set up the window
turtle.setup(640, 480)
# Create a turtle
turtle.Turtle()
# Set pen size to 3
turtle.pensize(3)
# Set drawing color to blue
turtle.pencolor("blue")
# Move the turtle forward by 100 units
turtle.forward(100)
# Turn the turtle right by 90 degrees
turtle.right(90)
# Move the turtle forward by 50 units
turtle.forward(50)
# Turn the turtle left by 90 degrees
turtle.left(90)
# Lift the pen up – no drawing when moving
turtle.penup()
# Move the turtle to a specific location
turtle.goto(52, 68)
# Put the pen down – drawing when moving
turtle.pendown()
# Draw a circle with radius of 25
turtle.circle(25)
# Draw a dot with diameter 10
turtle.dot(10)
# Set the turtle heading to 0 (East)
turtle.setheading(0)
# Change the turtle color
turtle.color("red")
# Draw a filled shape
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
# Clear the drawing
turtle.clear()
# Reset the turtle's state
turtle.reset()
# Hide the turtle
turtle.hideturtle()
# Display the turtle
turtle.showturtle()
# Set the animation speed (0:fastest, 1:slowest, 10:normal)
turtle.speed(5)
# Display text
turtle.write('Hello, World!')
# Get input with a dialog box
Color = turtle.textinput('Input', 'Pick a color')
# Respond to user input
turtle.color(f'{Color}')
# Filling a shape with color
turtle.hideturtle()
turtle.fillcolor(f'{Color}')
turtle.begin_fill() 
turtle.circle(50)
turtle.end_fill()
# Close the window on a click
turtle.done()

