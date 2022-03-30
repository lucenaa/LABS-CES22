import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def set_to_green(): # Set the fillcolor of tess to green
    tess.fillcolor("green")


def set_to_red(): # Set the fillcolor of tess to red
    tess.fillcolor("red")


def set_to_blue(): # Set the fillcolor of tess to blue
    tess.fillcolor("blue")


def set_to_neutral(): # Set the fillcolor of tess to blue
    tess.fillcolor("darkgrey")


def increase_shapesize(): # Increases the radius of the circle
    k = tess.shapesize()[0]
    if k < 4:
        k = k + 1
        tess.shapesize(k)


def decrease_shapesize(): # Decreases the radius of the circle
    k = tess.shapesize()[0]
    if k > 1:
        k = k - 1
        tess.shapesize(k)


def increase_pensize(): # Increases the pensize of Tess
    k = tess.pensize()
    if k < 20:
        k = k + 1
        tess.pensize(k)


def decrease_pensize(): # Decreases the pensize of Tess
    k = tess.pensize()
    if k > 1:
        k = k + 1
        tess.pensize(k)


# Bind the event handler to the space key, "r", "g", "b", "+", "-"
wn.onkey(advance_state_machine, "space")
wn.onkey(set_to_green, "g")
wn.onkey(set_to_red, "r")
wn.onkey(set_to_blue, "b")
wn.onkey(decrease_shapesize, "m")
wn.onkey(increase_shapesize, "p")
wn.onkey(set_to_neutral, "n")
wn.onkey(increase_pensize, "+")
wn.onkey(decrease_pensize, "-")


wn.listen() # Listen for events
wn.mainloop()