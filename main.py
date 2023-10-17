# steps:
# 1. create screen
# 2. 2 paddles either end of the screen controlled by 2 users
# 3. a ball that bounces and starts from center
# 4. scoreboard - increases when one player misses

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

screen.listen()
# paddle 1 go up and down
screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")

# paddle 2 go up and down
screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")

is_game_on = True

sleep_time = 0.1
while is_game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
        sleep_time *= 0.9
    if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        sleep_time *= 0.9

    # detect when ball misses right paddle
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()
        sleep_time = 0.1

    # detect when ball misses left paddle
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()
        sleep_time = 0.1

    # game over
    if scoreboard.game_over():
        is_game_on = False



screen.exitonclick()
