import turtle
import time
import random


delay = 0.5
score = 0
hgscr = 0
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("black")
wn.setup(width=600,height=660)
wn.tracer(0)

game_over = turtle.Turtle()
game_over.speed(5)
game_over.penup()
game_over.shape("square")
game_over.color("Red")
game_over.goto(0,0)
game_over.hideturtle()


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"




food = turtle.Turtle()
food.speed(0)
food.shapesize(0.7,0.7)
food.shape("circle")
food.color("#A8EBFF")
food.penup()
x = random.randint(-250, 250)
y = random.randint(-260, 260)
food.goto(x, y)

bodys = []
lin = turtle.Turtle()
lin.shape("circle")
lin.speed(0)
lin.color("white")
lin.penup()
lin.hideturtle()

for i in range(-300,280,+10):
    lin.goto(-300,i)
    lin.write("*",font=("Courier",18,"normal"))

for i in range(-300,280,+10):
    lin.goto(280,i)
    lin.write("*",font=("Courier",18,"normal"))

for i in range(-300,330,+10):
    lin.goto(i,280)
    lin.write("*",font=("Courier",18,"normal"))

for i in range(-330,330,+10):
    lin.goto(i,-300)
    lin.write("*",font=("Courier",18,"normal"))


pen = turtle.Turtle()
pen.shape("square")
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,-310)
pen.write("up:w    down:s    left:a    right:d    restart:q",align="center",font=("Courier",14,"normal"))
pen.goto(0,300)
pen.write("SCORE: 0\tHIGH SCORE: 0",align="center",font=("Courier",18,"normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.rt(90)


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def restart():
    head.showturtle()
    head.goto(0, 0)
    game_over.clear()
    food.showturtle()
    x = random.randint(-250, 250)
    y = random.randint(-260, 260)
    food.goto(x, y)


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(restart,"q")


while True:
    wn.update()
    pen.clear()
    pen.write("SCORE:0\tHIGH SCORE:0\t", align="center",font=("Courier", 18, "normal"))
    pen.goto(0, -310)
    pen.write("up:w    down:s    left:a    right:d    restart:q", align="center", font=("Courier", 14, "normal"))
    pen.goto(0, 300)

    if head.xcor()>250 or head.xcor()< -260 or head.ycor()>260 or head.ycor()<-260:
        game_over.pendown()
        game_over.write("GAME OVER", align="center", font=("Courier", 40, "bold"))
        head.hideturtle()
        food.hideturtle()
        head.penup()
        head.direction = "stop"
        for body in bodys:
            body.goto(1000, 1000)
        bodys.clear()
        score = 0
        delay = 0.5
        pen.clear()
        pen.goto(0, -310)
        pen.write("up:w    down:s    left:a    right:d    restart:q", align="center", font=("Courier", 14, "normal"))
        pen.goto(0, 300)
        pen.write("SCORE:{}\tHIGH SCORE:{}\t".format(score,hgscr), align="center", font=("Courier", 18, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-260, 260)
        food.goto(x, y)
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.shapesize(1, 1)
        new_body.color("#7AFE61")
        new_body.penup()
        bodys.append(new_body)
        score += 10
        if score % 20 == 0:
            delay = (delay*3)/4
        if score > hgscr:
            hgscr = score
        pen.clear()
        pen.goto(0, -310)
        pen.write("up:w    down:s    left:a    right:d    restart:q", align="center", font=("Courier", 14, "normal"))
        pen.goto(0, 300)
        pen.write("SCORE:{}\tHIGH SCORE:{}\t".format(score,hgscr), align="center", font=("Courier", 18, "normal"))

    for i in range(len(bodys)-1,0,-1):
        x = bodys[i-1].xcor()
        y = bodys[i-1].ycor()
        bodys[i].goto(x,y)

    if len(bodys) > 0:
        x = head.xcor()
        y = head.ycor()
        bodys[0].goto(x, y)


    move()


    for body in bodys:
        if body.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"
            for body in bodys:
                body.goto(1000, 1000)
            bodys.clear()
            score = 0
            delay = 0.5
            pen.clear()
            pen.clear()
            pen.goto(0, -310)
            pen.write("up:w    down:s    left:a    right:d    restart:q", align="center",font=("Courier", 14, "normal"))
            pen.goto(0, 300)
            pen.write("SCORE: {}     HIGH SCORE: {}".format(score,hgscr), align="center", font=("Courier", 18, "normal"))
            game_over.pendown()
            game_over.write("GAME OVER", align="center", font=("Courier", 40, "bold"))
    time.sleep(delay)

wn.mainloop()
