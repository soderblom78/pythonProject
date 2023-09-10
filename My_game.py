import time
import turtle
import math
import random
import winsound

# set up screen
wn = turtle.Screen()
wn.setup(600, 600)
wn.bgpic("images/space.gif")
wn.tracer(4)
fps = 60

# draw border
my_pen = turtle.Turtle()
my_pen.speed(100)
my_pen.penup()
my_pen.setposition(-300, - 300)
my_pen.pendown()
my_pen.pensize(3)
for side in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

# create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)

# create_score
score = 0
score_color = "white"

# create_goals
max_goals = 6
goals = []
for count in range(max_goals):
    goals.append(turtle.Turtle())
    goals[count].color("LightGoldenrod1")
    goals[count].shape("circle")
    goals[count].shapesize = 10
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-280, 280), random.randint(-280, 280))

# create_multiple enemy

max_enemy = 4
add_enemy = 0
extra_enemy = []

# set_up_time
start_time = time.time()
elapsed_time = time.time() - start_time
time_limit = 10

# timer_text_turtle
timer_text = turtle.Turtle()
timer_text.penup()
timer_text.hideturtle()
timer_text.color("White")
timer_text.setposition(0, 250)

# Print_timer_turtle
Print_timer_turtle = turtle.Turtle()
Print_timer_turtle.penup()
Print_timer_turtle.hideturtle()
Print_timer_turtle.color("White")
Print_timer_turtle.pensize(20)
Print_timer_turtle.setposition(-50, 250)
Print_timer_turtle.write("Timer ")

reset_timer = (int(time_limit - (time.time() - start_time)))

enemy = []
for count in range(max_enemy):
    enemy.append(turtle.Turtle())
    enemy[count].color("Red")
    enemy[count].shape("square")
    enemy[count].shapesize = 10
    enemy[count].penup()
    enemy[count].speed(0)
    enemy[count].setposition(random.randint(-280, 280), random.randint(-280, 280))





# set speed variable
speed = 1


# define functions
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


def is_goal_collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


def is_enemy_collision(e1, e2):
    d = math.sqrt(math.pow(e1.xcor() - e2.xcor(), 2) + math.pow(e1.ycor() - e2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


def is_extra_enemy_collision(e1, e2):
    d = math.sqrt(math.pow(e1.xcor() - e2.xcor(), 2) + math.pow(e1.ycor() - e2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


# set up keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")

while True:
    player.forward(speed)
    timer_text.write(int(time_limit - (time.time() - start_time)))

    if int(time_limit - (time.time() - start_time) <= 0):
        time_limit += 10
        add_enemy += 2

        for count in range(add_enemy):
            extra_enemy.append(turtle.Turtle())
            extra_enemy[count].color("Red")
            extra_enemy[count].shape("square")
            extra_enemy[count].shapesize = 10
            extra_enemy[count].penup()
            extra_enemy[count].speed(0)
            extra_enemy[count].setposition(random.randint(-280, 280), random.randint(-280, 280))

    for count in range(add_enemy):
        extra_enemy[count].forward(3)

        if extra_enemy[count].xcor() > 280 or extra_enemy[count].xcor() < -280:
            extra_enemy[count].right(180)

        if extra_enemy[count].ycor() > 280 or extra_enemy[count].ycor() < -280:
            extra_enemy[count].right(180)

        if is_extra_enemy_collision(player, extra_enemy[count]):
            extra_enemy[count].setposition(random.randint(-280, 280), random.randint(-280, 280))
            extra_enemy[count].right(random.randint(0, 360))
            score -= 1
            winsound.Beep(300, 300)

    # Boundary_Checking
    if player.xcor() > 280 or player.xcor() < -280:
        player.right(180)
        winsound.Beep(400, 50)

    if player.ycor() > 280 or player.ycor() < -280:
        player.right(180)
        winsound.Beep(400, 50)

    # move_the_goals
    for count in range(max_goals):
        goals[count].forward(3)

        # Boundary_Checking
        if goals[count].xcor() > 280 or goals[count].xcor() < -280:
            goals[count].right(180)

        if goals[count].ycor() > 280 or goals[count].ycor() < -280:
            goals[count].right(180)

        # Collision checking
        if is_goal_collision(player, goals[count]):
            goals[count].setposition(random.randint(-280, 280), random.randint(-280, 280))
            goals[count].right(random.randint(0, 360))
            score += 1
            winsound.Beep(750, 50)

    # move_the_enemy
    for count in range(max_enemy):
        enemy[count].forward(3)

        # Boundary_Checking
        if enemy[count].xcor() > 280 or enemy[count].xcor() < -280:
            enemy[count].right(180)

        if enemy[count].ycor() > 280 or enemy[count].ycor() < -280:
            enemy[count].right(180)

        if is_enemy_collision(player, enemy[count]):
            enemy[count].setposition(random.randint(-280, 280), random.randint(-280, 280))
            enemy[count].right(random.randint(0, 360))
            score -= 1
            winsound.Beep(300, 300)

    # draw the score to the board
    my_pen.undo()
    my_pen.penup()
    my_pen.hideturtle()
    my_pen.setposition(- 200, 250)
    my_pen.color("white")
    score_string = "Score: %s" % score
    my_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

    timer_text.clear()

    delay = input("Press Enter to finish.")
