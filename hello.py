import turtle

# set up screen
wn = turtle.Screen()

wn.window_width = 600
wn.window_height = 600
wn.setup(wn.window_width, wn.window_height)
print(wn.window_width, wn.window_width)


wn.title("Roger")

# images
wn.register_shape("images/cloud-nature.gif")
images = turtle.Turtle()
images.penup()
images.dx = 0
images.shape("images/cloud-nature.gif")
images.setposition(300, 300)

wn.bgcolor("lightskyblue")


wn.tracer = 0



x = -250
y = 200
letters = ["A", "B", "C", "D", "E"]
t = 0


# set up text boxes
tb = turtle.Turtle()


def box():
    tb.color("black")
    tb.fillcolor("yellow")
    tb.begin_fill()
    tb.pensize(3)
    tb.speed(0)
    tb.penup()
    tb.setposition(x, y)
    tb.pendown()
    for side in range(4):
        tb.forward(50)
        tb.left(90)

    tb.write("    " + letters[t], align="left", font=("Arial", 14, "normal"))
    tb.end_fill()
    tb.hideturtle()


for boxes in range(5):
    if boxes > 0:
        t += 1

    box()
    x += 80

clicks = 0
pen = turtle.Turtle()
pen.penup()
pen.goto(0, 100)
pen.color("white")
pen.hideturtle()
pen.write(f"Clicks: {clicks}", align="left", font=("Arial", 14, "normal"))


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("green")
        self.frame = 0
        self.speed = 0

        self.frames = ["square", "circle"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])

        wn.ontimer(self.animate, 500)


player = Player()
player.animate()


def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="left", font=("Arial", 14, "normal"))
    player.goto(0, -100)


player.onclick(clicked)

player.dy = 0
player.dx = 0
player. height = 20
player.width = 20
player.state = "ready"
speed = 1

gravity = -0.8


def jump():
    if player.state == "ready":
        player.dy = 12
        player.state = "jumping"


def move_forward():
    if player.state != "jumping":
        player.color("light green")
        player.forward(3)


def move_back():
    if player.state != "jumping":
        player.color("light green")
        player.back(3)


def increase_speed():
    global speed
    speed += 1


wn.onkeypress(jump, "space")
wn.onkeypress(move_forward, "Right")
wn.onkeypress(move_back, "Left")
wn.onkeypress(increase_speed, "Up")
wn.listen()


player2 = Player()
player2.goto(-100, 0)
player2.color("yellow")
player2.animate()

player3 = Player()
player3.goto(-200, 0)
player3.color("blue")
player3.animate()


while True:
    if images.xcor() < -440:
        images.hideturtle = True

    player.forward(speed)
    images.penup()
    images.back(speed)
    x = images.xcor()
    x -= images.dx
    images.setx(x)
    images.hideturtle = False







    player.dy += gravity
    y = player.ycor()
    y += player.dy
    player.sety(y)

    if player.ycor() < -100 + player.height / 2:
        player.sety(-100 + player.height / 2)
        player.dy = 0
        player.state = "ready"
    wn.update()







