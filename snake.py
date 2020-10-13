import random

import pygame
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 20 * 20, y // 20 * 20


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200, 200), (220, 200), (240, 200)]
snake_head = pygame.Surface((20, 20))
snake_head.fill((0, 128, 0))
snake_skin = pygame.Surface((20, 20))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((20, 20))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()
game_over = False


while True:
    clock.tick(10)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        # score = score + 1

        # Check if snake collided with boundaries
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

        # Check if the snake has hit itself
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)


    for i in snake[:1]:
        screen.blit(snake_head, i)

    for i in snake[2:]:
        screen.blit(snake_skin, i)

    pygame.display.update()
