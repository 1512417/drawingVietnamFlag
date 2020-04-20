import turtle
wn = turtle.Screen()            # Set up the window and its attributes
wn.bgcolor("red")               # Background color of the screen
screen_width = 750;             # Width of the screen
screen_height = 500;            # Height of the screen
star_length = 200;              # Length of one side of the star
 
wn.setup(width = screen_width, height = screen_height)
wn.title("Flag of Vietnam")
 
vin = turtle.Turtle()
vin.color("red")                # Set the color of the turtle to red
# Move the turtle to a predefined coordinate
vin.setx((screen_width - star_length)/2 - screen_width/2)
vin.sety(star_length/4)
vin.color("yellow")
vin.shape("turtle")              # Hide the shape of the turtle
vin.pensize(3)                  # Pen size of the turtle
vin.speed(2)
# Draw the flag
for counter in range(5):
    vin.forward(star_length)                 
    vin.right(144)
vin.goto((screen_width - star_length)/2 - screen_width/2,star_length/4)
vin.setheading(0)
vin.pendown()
vin.begin_fill()
vin.color("yellow")
for turn in range(0,5) :
    vin.forward(star_length)
    vin.right(144)
    vin.forward(star_length)
    vin.right(144)
vin.end_fill()
vin.penup()
vin.shape("blank")    
wn.exitonclick()