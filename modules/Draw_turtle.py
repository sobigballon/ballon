import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_turtle():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    for j in range(37):
        draw_square(brad)
        brad.right(10)
    #brad.forward(100)
    #brad.right(120)
    #brad.forward(100)
    #brad.right(120)
    #brad.forward(100)
    #brad.right(120)
    #brad.forward(100)
    #brad.right(90)

    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    

    window.exitonclick()

draw_turtle()
