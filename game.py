import pygame
import time
import random

pygame.init()

# Window size and colors
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)

# Creating the window
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Frame rate
clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [width / 6, height / 3])

def gameLoop():
    # initialize the game
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Creating food at random position
    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    snake_List = []
    Length_of_snake = 1

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # Check if snake hits the wall
        if x1 >= width:
            x1 = 0
        elif x1 < 0:
            x1 = width - snake_size
        elif y1 >= height:
            y1 = 0
        elif y1 < 0:
            y1 = height - snake_size

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Create a new block for the snake's head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove the last block of the snake if it does not hit the food
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake hits the food
        if x1 == foodx and y1 == foody:
            # Generate new food
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Draw the snake
        display.fill(white)
        for segment in snake_List:
            pygame.draw.rect(display, black, [segment[0], segment[1], snake_size, snake_size])

        pygame.draw.rect(display, green, [foodx, foody, snake_size, snake_size])
        pygame.display.update()

        # Check if the snake hits itself
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Frame rate
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

gameLoop()

