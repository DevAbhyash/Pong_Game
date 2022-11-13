import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score

from turtle import Turtle
screen=turtle.Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
r_paddle =Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()






screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball_y_cor = ball.ycor()
    if ball_y_cor>280 or ball_y_cor<-280:
      ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
     ball.bounce_x()

    #No collison with right paddle
    if ball.xcor()>340:
        ball.reset()
        score.l_point()
        ball.speed()

    #No collison with left paddle
    if ball.xcor()<-340:
        ball.reset()
        score.r_point()
        ball.speed()






screen.exitonclick()