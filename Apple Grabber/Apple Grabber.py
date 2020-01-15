import turtle
from random import randint
import time
import winsound
import random
import keyboard

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

wn = turtle.Screen()
wn.title("Apple grabber")
wn.setup(width=1500, height=800)

# score default
global score

# default var settings
global t
global start_time
global col_w
global col_a
global col_b
global death
global keep_looping
global game_play

game_play = True
keep_looping = True
col_w = False
col_a = False
col_b = False
death = False
apple_positions = [(10000, 0)]
napple_positions = [(0, 100000)]


# player setup
def make_player():
    global turtle_obj
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    turtle_obj.shape("square")
    turtle_obj.shapesize(stretch_wid=1, stretch_len=2)
    turtle_obj.color("lime green")
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(90)


# Score block
def make_score():
    global pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.color("white")
    pen.goto(0, 325)
    pen.write("Score: 0", align="center", font=("Courier", 18, "normal"))


# right wall
global a
global b
a = 750
b = 0


def rw_build():
    rw = turtle.Turtle()
    rw.speed(0)
    rw.shape("square")
    rw.shapesize(stretch_wid=41, stretch_len=1)
    rw.color("white")
    rw.penup()
    rw.goto(int(a), int(b))


# left wall
def lw_build():
    lw = turtle.Turtle()
    lw.speed(0)
    lw.shape("square")
    lw.shapesize(stretch_wid=41, stretch_len=1)
    lw.color("white")
    lw.penup()
    lw.goto(int(-a), int(b))


# top wall
global c
global d
c = 0
d = 400

def tw_build():
    tw = turtle.Turtle()
    tw.speed(0)
    tw.shape("square")
    tw.shapesize(stretch_wid=1, stretch_len=75)
    tw.color("white")
    tw.penup()
    tw.goto(int(c), int(d))


# bottom wall
def bw_build():
    bw = turtle.Turtle()
    bw.speed(0)
    bw.shape("square")
    bw.shapesize(stretch_wid=1, stretch_len=75)
    bw.color("white")
    bw.penup()
    bw.goto(int(c), int(-d))


# build walls

def build_walls():
    rw_build()
    lw_build()
    tw_build()
    bw_build()


# Movement functions
def t_cw():
    turtle_obj.right(22.5)
    winsound.PlaySound("blip noise", winsound.SND_ASYNC)


def t_ccw():
    turtle_obj.left(22.5)
    winsound.PlaySound("blip noise", winsound.SND_ASYNC)


def t_fw():
    turtle_obj.forward(22.5)


def t_dw():
    turtle_obj.backward(22.5)


# noinspection DuplicatedCode
def new_apple():
    global napple
    napple = turtle.Turtle()
    napple.speed(0)
    napple.penup()
    napple.color(random.choice(colors))
    napple.shape("circle")
    napple.goto(randint(-a + 25, a - 25), randint(-d + 25, d - 25))
    napple_positions.insert(0, napple.pos())


# apple removal after collection
def move_napple():
    napple.goto(100000, 0)


def end_loop():
    global keep_looping
    global death
    global col_w
    while keep_looping:
        for i in range(1):
            pen.clear()
            pen.goto(0, 0)
            pen.write("YOU DIED!", align="center", font=("Courier", 48, "bold"))
            time.sleep(5)
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 48, "bold"))
            time.sleep(3)
            # noinspection PyUnresolvedReferences
            turtle.clearscreen()
            wn.bgcolor("black")
            wn.tracer(0)
        break
    pen.clear()
    for i in range(1000):
        pen.goto(0, 0)
        pen.write("If you want to play again,\n   press the \"R\" key.", align="center", font=("Courier", 48, "bold"))
        try:
            if keyboard.is_pressed("r"):
                turtle.clearscreen()
                death = False
                col_w = False
                start_game()
                break
        except:
            print("")


def endgame():
    while death:
        end_loop()


# timer
def clock():
    timer = turtle.Turtle()
    timer.speed(0)
    timer.penup()
    timer.hideturtle()
    timer.goto(700, 325)
    timer.color("white")
    timer.write(int(e), align="right", font=("Courier", 18, "normal"))
    timer.clear()


# first apple
def make_first_apple():
    global apple
    apple = turtle.Turtle()
    apple.speed(0)
    apple.penup()
    apple.color("red")
    apple.shape("circle")
    apple.goto(randint(-a + 25, a - 25), randint(-d + 25, d - 25))
    apple_positions.insert(0, apple.pos())


# timer setup
def start_timer():
    global start_time
    global t
    start_time = time.time()
    t = time.time() - start_time


def start_game():
    global game_play
    global score
    global t
    global e
    e = 0
    t = 0
    score = 0
    game_play = True
    wn.bgcolor("black")
    wn.tracer(0)
    make_player()
    build_walls()
    make_score()
    start_timer()
    make_first_apple()
    wn.listen()
    wn.onkeyrelease(t_cw, "d")
    wn.onkeyrelease(t_ccw, "a")
    wn.onkeypress(t_fw, "w")


start_game()

while game_play:

    # top wall collision
    if turtle_obj.ycor() > d - 15:
        col_w = True

    # bottom wall collision
    if turtle_obj.ycor() < -d + 15:
        col_w = True

    # left wall collision
    if turtle_obj.xcor() < -a + 15:
        col_w = True

    # right wall collision
    if turtle_obj.xcor() > a - 15:
        col_w = True

    # death by wall collision
    if col_w:
        winsound.PlaySound("death sound 2", winsound.SND_ASYNC)
        time.sleep(3)
        death = True
        endgame()

    # apple collection mechanics
    if turtle_obj.distance(apple_positions[0]) < 27:
        col_a = True

    if turtle_obj.distance(apple_positions[0]) > 27:
        col_a = False

    if turtle_obj.distance(napple_positions[0]) < 27:
        col_b = True

    if turtle_obj.distance(napple_positions[0]) > 27:
        col_b = False

    # 1st apple collection
    if col_a and score == 0:
        winsound.PlaySound("score blip", winsound.SND_ASYNC)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        apple.goto(20000, 10000)
        new_apple()
        start_time = time.time()

    # additional apple collection
    if col_b and score >= 1:
        winsound.PlaySound("score blip", winsound.SND_ASYNC)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        move_napple()
        new_apple()
        start_time = time.time()

    # timer mechanic implementation
    t = -(start_time - time.time())
    e = t
    clock()

    # death by time
    if e > 10:
        death = True
        winsound.PlaySound("death sound 2", winsound.SND_ASYNC)
        endgame()
    if e > 7 and score > 5:
        death = True
        winsound.PlaySound("death sound 2", winsound.SND_ASYNC)
        endgame()
    if e > 5 and score >= 10:
        death = True
        winsound.PlaySound("death sound 2", winsound.SND_ASYNC)
        endgame()

    wn.update()
