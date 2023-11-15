from turtle import Screen
from pong_parts import Parts
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width = 1000, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_player = Paddle((-450, 0))
right_player = Paddle((450, 0))
ball = Ball()
pong_parts = Parts()

pong_parts.centre_dots()

screen.listen()
screen.onkey(left_player.goUP, "w")
screen.onkey(left_player.goDOWN, "s")
screen.onkey(right_player.goUP, "Up")
screen.onkey(right_player.goDOWN, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_player) < 50 and ball.xcor() > 420 or ball.distance(left_player) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    if ball.xcor() > 480:
        ball.reset_position()

    if ball.xcor() < -480:
        ball.reset_position()


screen.exitonclick()


