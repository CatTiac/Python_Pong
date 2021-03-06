import turtle
import winsound

window = turtle.Screen()
window.title("Pong by @CatTiac")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_1 = 0
score_2 = 0

#Paddle 1 (Capital T is a class name)
paddle_1= turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#Paddle 2
paddle_2= turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#Ball movement (e.g. xspeed = x axis)
ball.xspeed = 0.5
ball.yspeed = 0.5

#Score Pen
pen = turtle.Turtle()
#Animation speed
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 24, "normal"))

#Function (paddle movements)
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#Keyboard binding
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")



#Main game loop
while True:
    window.update()

    #Moving ball
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xspeed *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("cheer.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xspeed *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("cheer2.wav", winsound.SND_ASYNC)

    #Paddle/Ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.xspeed *= -1
        winsound.PlaySound("oneUp.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.xspeed *= -1
        winsound.PlaySound("oneUp.wav", winsound.SND_ASYNC)
