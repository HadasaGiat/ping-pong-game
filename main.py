import turtle as t
import os
player_a_score=0
player_b_score=0


win=t.Screen()
win.title("ping pong!!")
win.bgcolor("#112233")
win.setup(width=850,height=600)
win.tracer(0)

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("red")
paddle_left.shapesize(stretch_wid=3,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("red")
paddle_right.shapesize(stretch_wid=3,stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball_dx=0.5
ball_dy=0.5

pen=t.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {player_a_score}\t\tPlayer B: {player_b_score}",align="center",font=("Courier",24,"bold"))

def paddle_left_up():
    y=paddle_left.ycor()
    y+=25
    paddle_left.sety(y)
    if paddle_left.ycor() > 290:
        paddle_left.sety(290)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= 25
    paddle_left.sety(y)
    if paddle_left.ycor() < -290:
        paddle_left.sety(-290)

def paddle_right_up():
    y=paddle_right.ycor()
    y+=25
    paddle_right.sety(y)
    if paddle_right.ycor() > 290:
        paddle_right.sety(290)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 25
    paddle_right.sety(y)
    if paddle_right.ycor() < -290:
        paddle_right.sety(-290)

win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")

while True:
    win.update()
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball_dy*=-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball_dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball_dx *= -1
        player_a_score+=1
        pen.clear()
        pen.write(f"Player A: {player_a_score}\t\tPlayer B: {player_b_score}", align="center",
                  font=("Courier", 24, "bold"))
        # os.system("afplay wallhit.wav")

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball_dx *= -1
        player_b_score+=1
        pen.clear()
        pen.write(f"Player A: {player_a_score}\t\tPlayer B: {player_b_score}", align="center",
                  font=("Courier", 24, "bold"))
        # os.system("afplay wallhit.wav")

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and
            ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and
            ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx *= -1

win.update()


os.system("pause")