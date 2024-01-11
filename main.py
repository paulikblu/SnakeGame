from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Paul's snake")
screen.tracer(0)

def snake_game():
    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.point()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.game_over()
            game_is_on = False

        for body in snake.bodies[1:]:
            if snake.head.distance(body) < 10:
                score.game_over()
                game_is_on = False

    new_game = screen.textinput("New Game", "Do you want to start a new game? yes/no",)
    if new_game == "yes":
        screen.reset()
        snake_game()

snake_game()

screen.exitonclick()