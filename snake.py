
# importing libraries
import pygame
import sys
import pygame_gui
import time
import random
from leaderboard import start_leaderboard




def show_score(choice, color, font, size,score,game_window):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over(game_window,score):

    # creating font object my_font


    # after 2 seconds we will quit the
    # program
    start_leaderboard(score,game_window,game_start)
    # deactivating pygame library
    #pygame.quit()

    # quit the program
    #quit()
# Main Function

def game_start():
    print("game has started")
    snake_speed = 15
    fps = pygame.time.Clock()

    # Window size
    window_x = 800
    window_y = 600

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    pygame.init()


    pygame.display.set_caption('GeeksforGeeks Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))
    manager = pygame_gui.UIManager((window_x, window_y))
    game_started = True


    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake
    # body
    snake_body = [  [100, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                      random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # setting default snake direction
    # towards right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0
    while game_started:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two directions
        # simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores will be
        # incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                              random.randrange(1, (window_y//10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(
              pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(
          fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over(game_window,score)
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over(game_window,score)

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window,score)

        # displaying score countinuously
        show_score(1, white, 'times new roman', 20,score,game_window)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)
game_start()
