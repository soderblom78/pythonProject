import turtle

# set up screen
wn = turtle.Screen()
wn.title("Roger")
wn.bgcolor("black")
wn.tracer = 0

player = turtle.Turtle()
player.shape("square")
player.color("yellow")
player.dy = 0
player.speed(0)
player.penup()


def jump():
    player.dy = 5


wn.listen()
wn.onkey(jump, "space")


while True:
    y = player.ycor()
    y += player.dy
    player.sety(y)

    wn.update()



