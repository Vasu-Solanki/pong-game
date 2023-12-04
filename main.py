from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Initializing a screen window.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong: Arcade Game")
screen.bgcolor("black")
screen.tracer(0)

# Initializing the control of the paddle
right_paddle = Paddle(350)
left_paddle = Paddle(-350)

# Initializing ball.
ball = Ball()

# score board.
score = ScoreBoard()


game_is_on = True
# controller of the paddle.
right_paddle.controller(key_for_up="Up", key_for_down="Down")
left_paddle.controller(key_for_down="s", key_for_up="w")


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_go()
    score.update_score()

    # check if ball hit the side corners.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()

    # check if the ball hit the paddle.
    if right_paddle.distance(ball) < 50 and ball.xcor() < 340 or ball.distance(left_paddle) < 50 and ball.xcor() > -340:
        ball.hit_paddle()

    if ball.xcor() > 380:
        ball.miss()
        score.right_score()

    if ball.xcor() < -380:
        ball.miss()
        score.left_score()

screen.exitonclick()
