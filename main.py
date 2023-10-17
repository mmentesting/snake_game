from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=410, height=410)
screen.bgcolor("gray20")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 10:
        food.change_position()
        food.change_color()
        snake.extend_snake()
        score_board.track_score()
    if snake.head.xcor() > 199 or snake.head.xcor() < -199 or snake.head.ycor() > 199 or snake.head.ycor() < -199:
        score_board.reset_scoreboard()
        snake.reset_snake()
    for segment in snake.s_segments[1:]:
        if snake.head.distance(segment) < 5:
            score_board.reset_scoreboard()
            snake.reset_snake()
    if score_board.lives == 0:
        game_on = False
        score_board.game_over()

screen.exitonclick()
