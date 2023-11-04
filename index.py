# Import Libraries

from turtle import *
from time import *
from random import *

# Define Variables

delay_turtle = 0.1

user_score = 0
high_user_score = 0

# Define Screen

client_window = Screen()
client_window.title('Snake, An Epic Come Back')
client_window.bgcolor('#289519')
client_window.setup(width=1280, height=720)

# !!! DON'T FORGET TO USE ZERO IN FRACTIONS !!!

#client_window.tracer(0)

# Create Snake's Head

snake_head = Turtle()
snake_head.color('#fafafa')
snake_head.shape('square')
snake_head.penup()
snake_head.home()

snake_head.direction = 'stop'

# Apples

apple_food = Turtle()
apple_colours = choice(['#febf20', '#f25a0e', '#fe1e1a', '#b81e46', '#1c50d6'])
apple_shapes = choice(['triangle', 'square', 'circle'])
apple_food.speed(0)
apple_food.shape(apple_shapes)
apple_food.color(apple_colours)
apple_food.penup()
apple_food.goto(0, 200)

# Text

pen = Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color('#FAFAFA')
pen.goto(0, 590)
pen.write('Score: 0 │ Highscore: 0', align='center', font='Inter 24 bold')

# Snake Movement

def snake_up():
    if snake_head.direction != 'down':
        snake_head.direction == 'up'

def snake_down():
    if snake_head.direction != 'up':
        snake_head.direction == 'down'

def snake_left():
    if snake_head.direction != 'left':
        snake_head.direction == 'right'

def snake_right():
    if snake_head.direction != 'right':
        snake_head.direction == 'left'

def snake_move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y+20)

    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y-20)

    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 20)

    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 20)

# Button Movement

client_window.listen()
client_window.onkeypress(snake_up, 'w')
client_window.onkeypress(snake_down, 's')
client_window.onkeypress(snake_left, 'a')
client_window.onkeypress(snake_right, 'd')

# Snake Segments

snake_segments = []

# Game in itself

while True:
    client_window.update()

    if snake_head.xcor() > 630 or snake_head.xcor() < -630 or snake_head.ycor() > 350 or snake_head.ycor() < -350:
        sleep(1)
        snake_head.home()

        apple_food.direction = 'stop'
        apple_food.shape(apple_shapes)
        apple_food.color(apple_colours)

        for i in snake_segments:
            snake_segments.goto(5000, 5000)

        snake_segments.clear()
        user_score = 0
        delay_turtle = 0.1
        pen.clear()

        pen.write(f'Score: {user_score} │ Highscore: {high_user_score}', align='center',
                  font='Inter 24 bold')

    if snake_head.distance(apple_food) < 20:
        apple_food.goto(randint(-600, 600), randint(-350, 350))

        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.color('#febf20')
        new_segment.shape('square')
        new_segment.penup()

        snake_segments.append(new_segment)

        delay_turtle -= 0.001

        user_score += 1

        if user_score > high_user_score:
            high_user_score = user_score

        pen.clear()

        pen.write(f'Score: {user_score} │ Highscore: {high_user_score}', align='center',
                  font='Inter, 24, bold')

    for j in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[j-1].xcor()
        y = snake_segments[j-1].ycor()
        snake_segments[j].goto(x, y)

    if len(snake_segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_segments[0].goto(x, y)

    snake_move()

    for i in snake_segments:
        if i.distance(snake_head) < 20:
            sleep(1)
            snake_head.home()

            snake_head.direction('stop')
            apple_colours = choice(['#febf20', '#f25a0e', '#fe1e1a', '#b81e46', '#1c50d6'])
            apple_shapes = choice(['triangle', 'square', 'circle'])

            for i in snake_segments:
                snake_segments.goto(5000, 5000)

            snake_segments.clear()
            user_score = 0
            delay_turtle = 0.1
            pen.clear()

            pen.write(f'Score: {user_score} │ Highscore: {high_user_score}', align='center',
                      font='Inter 24 bold')

    sleep(delay_turtle)