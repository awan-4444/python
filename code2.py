import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Drawing")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(5)

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Move to a new position
pen.penup()
pen.goto(-150, 150)
pen.pendown()

# Draw a circle
pen.circle(50)

# Move to another position
pen.penup()
pen.goto(150, -150)
pen.pendown()

# Draw a triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Finish
pen.hideturtle()
screen.mainloop()