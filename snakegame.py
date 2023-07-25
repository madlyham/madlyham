from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00b894"
FOOD_COLOR = "#d63031"
BACKGROUND_COLOR = "#2d3436"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y,
                                             x + SPACE_SIZE, y + SPACE_SIZE,
                                             fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global score
    global GAME_WIDTH, GAME_HEIGHT

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y,
                                     x + SPACE_SIZE, y + SPACE_SIZE,
                                     fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    elif x < 0:
        x = 650

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y,
                                         x + SPACE_SIZE, y + SPACE_SIZE,
                                         fill=SNAKE_COLOR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]
        window.after(SPEED, next_turn, snake, food)
    elif x >= GAME_WIDTH:
        x = 0
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y,
                                         x + SPACE_SIZE, y + SPACE_SIZE,
                                         fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]
        window.after(SPEED, next_turn, snake, food)
    elif y < 0:
        y = 650
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y,
                                         x + SPACE_SIZE, y + SPACE_SIZE,
                                         fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]
        window.after(SPEED, next_turn, snake, food)
    elif y >= GAME_HEIGHT:
        y = 0
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y,
                                         x + SPACE_SIZE, y + SPACE_SIZE,
                                         fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        window.after(SPEED, next_turn, snake, food)
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    global retry_window

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER",
                       fill="red", tag="gameover")

    retry_window = Tk()
    retry = Button(retry_window, text='retry', command=reset,
                   font=('Ink Free', 40, 'bold'),
                   bg='#5a5a5a', fg='white')
    retry.pack()
    retry_window.mainloop()
    print(f'your score is: {score}')


def reset():
    global Snake
    global Food
    global snake
    global food
    global next_turn
    global retry_window
    global score

    score = 0
    label.config(text="Score:{}".format(score))
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    canvas.delete('gameover')
    retry_window.destroy()


window = Tk()
window.title("Snake game")
window.resizable(False, False)
window.config(bg='#5a5a5a')

score = 0
direction = 'left'

label = Label(window,
              text="Score:{}".format(score),
              font=('Ink Free', 40, 'bold'),
              bg='#5a5a5a',
              fg='white')
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
