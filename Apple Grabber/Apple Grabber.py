import turtle
from random import randint
import time
import winsound
import sys

wn = turtle.Screen()
wn.title("Apple grabber")
wn.setup(width=1500, height=800)
wn.bgcolor("black")
wn.tracer(0)

# score default
score = 0

# default var settings
global t
global start_time
global col_w
global col_a
global col_b
global death
col_w = False
col_a = False
col_b = False
death = False
apple_positions = [(10000, 0)]
napple_positions = [(0, 100000)]

# player setup
turtle_obj = turtle.Turtle()
turtle_obj.speed(0)
turtle_obj.shape("square")
turtle_obj.shapesize(stretch_wid=1, stretch_len=2)
turtle_obj.color("lime green")
turtle_obj.goto(0, 0)
turtle_obj.setheading(90)

# Score block
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
rw = turtle.Turtle()
rw.speed(0)
rw.shape("square")
rw.shapesize(stretch_wid=41, stretch_len=1)
rw.color("white")
rw.penup()
rw.goto(int(a), int(b))

# left wall
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
top_w = turtle.Turtle()
top_w.speed(0)
top_w.shape("square")
top_w.shapesize(stretch_wid=1, stretch_len=75)
top_w.color("white")
top_w.penup()
top_w.goto(int(c), int(d))

# bottom wall
bot_w = turtle.Turtle()
bot_w.speed(0)
bot_w.shape("square")
bot_w.shapesize(stretch_wid=1, stretch_len=75)
bot_w.color("white")
bot_w.penup()
bot_w.goto(int(c), int(-d))

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

# Movement controls
wn.listen()
wn.onkeyrelease(t_cw, "d")
wn.onkeyrelease(t_ccw, "a")
wn.onkeypress(t_fw, "w")

def new_apple():
    global napple
    napple = turtle.Turtle()
    napple.speed(0)
    napple.penup()
    napple.color("red")
    napple.shape("circle")
    napple.goto(randint(-a + 25, a - 25), randint(-d + 25, d - 25))
    napple_positions.insert(0, napple.pos())

# apple removal after collection
def move_napple():
    napple.goto(100000, 0)

def end_loop():
    for i in range(5):
        pen.clear()
        pen.goto(0, 0)
        pen.write("YOU DIED!", align="center", font=("Courier", 48, "bold"))
        time.sleep(5)
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 48, "bold"))
        time.sleep(3)
        turtle.clearscreen()
        wn.bgcolor("black")
        wn.tracer(0)
    sys.exit()

def endgame():
    while death == True:
        end_loop()

def alt_end_loop():
    for i in range(5):
        pen.clear()
        pen.goto(0, 0)
        pen.write("YOU'RE TOO SLOW!", align="center", font=("Courier", 48, "bold"))
        time.sleep(5)
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 48, "bold"))
        time.sleep(3)
        turtle.clearscreen()
        wn.bgcolor("black")
        wn.tracer(0)
    sys.exit()

def endgame_alt():
    while death == True:
        winsound.PlaySound("death sound 2", winsound.SND_ASYNC)
        alt_end_loop()

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
apple = turtle.Turtle()
apple.speed(0)
apple.penup()
apple.color("red")
apple.shape("circle")
apple.goto(randint(-a + 25, a - 25), randint(-d + 25, d - 25))
apple_positions.insert(0, apple.pos())

# timer setup
start_time = time.time()
t = time.time() - start_time

while True:
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
    if col_w == True:
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
    if col_a == True and score == 0:
        winsound.PlaySound("score blip", winsound.SND_ASYNC)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        apple.goto(10000, 10000)
        new_apple()
        start_time = time.time()

    # additional apple collection
    if col_b == True and score >= 1:
        winsound.PlaySound("score blip", winsound.SND_ASYNC)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        move_napple()
        new_apple()
        start_time = time.time()

    # time mechanics
    t = -(start_time - time.time())
    e = t
    clock()
    
    #death by time
    '''if e > 10:
        death = True
        endgame_alt()
    if e > 7 and score > 5:
        death = True
        endgame_alt()
    if e > 5 and score >= 10:
        death = True
        endgame_alt()'''

    wn.update()