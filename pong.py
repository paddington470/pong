import turtle

#window
win = turtle.Screen()
win.title("pong by izz")
win.bgcolor(color)
win.setup(width=800, height=600)

# score
score_a = 0 #starting scor
score_b = 0

#  paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") 
paddle_a.color("white") 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#  paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#  ball
ball = turtle.Turtle()
ball.speed(0) # starting speed of ball
ball.shape("square") # shape of ball, # circle , triangle
ball.color("white") # color of ball #pine
ball.goto(0, 0) #were the ball starts 
ball.penup() #dose not make lines
ball.dx = 2 #were it moves on the x axish firset 
ball.dy = 2 #the same as the other on but for y
# pen=scor
pen = turtle.Turtle()

pen.speed(0)
pen.color("white")#scor coloer # pink
pen.penup()
pen.hideturtle()
pen.goto(0, -280)
pen.write("player A:0  player B  0", align="center", font=("courier", 18, "normal"))


# function
def paddle_a_up():
    y = paddle_a.ycor() #move up
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor() #move down
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binging
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# main gAME LOOP
while True:
    win.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx) #keep moveing on the x
    ball.sety(ball.ycor() + ball.dy) #keep moveing on the y 

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -270:
        ball.sety(-270)
        ball.dy *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if paddle_a.ycor() < -270:
        paddle_a.sety(-270)

    if paddle_a.ycor() > 270:
        paddle_a.sety(270)

    if paddle_b.ycor() < -270:
        paddle_b.sety(-270)

    if paddle_b.ycor() > 270:
        paddle_b.sety(270)
    # B
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx += 0.5#speed added to it aftere beating it 
        ball.dy += -0.5
        ball.dx *= -1#so it go the other way
        score_a += 1
        pen.clear()
        pen.write("player A:{}  player B  {}".format(score_a, score_b), align="center", font=("courier", 18, "normal"))

    # A
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx += -0.5
        ball.dy += -0.5
        ball.dx *= -1
        score_b += 1 # add to scor
        pen.clear()
        pen.write("player A:{}  player B  {}".format(score_a, score_b), align="center", font=("courier", 18, "normal"))
        ball.dx += 1
        ball.dy += 1

    # paddle and ball culide
    if 330 < ball.xcor() < 360 and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):#the bangere line
        ball.setx(330)
        ball.dx *= -1

    if -330 > ball.xcor() > -350 and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

