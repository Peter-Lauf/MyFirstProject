import pygame
import sys
import numpy as np
from pygame import sysfont

pygame.init()

WIDTH = 800
HEIGHT = 800
LINE_WIDTH = 10
BOARD_ROWS = 8
BOARD_COLUMNS = 8
CIRCLE_RADIUS = 35
CIRCLE_WIDTH = 10
X_WIDTH = 18
SPACE = 18
# FPS = 60
CIRCLE_COLOUR = (238, 64, 0)
X_COLOUR = (51, 161, 201)
BG_COLOUR = (255, 211, 155)
LINE_COLOUR = (61, 61, 61)
TEXT_COLOUR = (240, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PETER'S TIC TAC TOE - CODING IS LIKE STUBBING MY TOE")
screen.fill(BG_COLOUR)

# The board
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS), dtype='int16')


def draw_lines():

    # Horizontal Lines
    pygame.draw.line(screen, LINE_COLOUR, (0, 0), (800, 0), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 100), (800, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 200), (800, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 300), (800, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 400), (800, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 500), (800, 500), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 600), (800, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 700), (800, 700), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 800), (800, 800), LINE_WIDTH)


    # Vertical lines
    pygame.draw.line(screen, LINE_COLOUR, (0, 0), (0, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (100, 0), (100, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (200, 0), (200, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (300, 0), (300, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (400, 0), (400, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (500, 0), (500, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (600, 0), (600, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (700, 0), (700, 800), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (800, 0), (800, 800), LINE_WIDTH)



def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                # Making sure that the figures are in the center of the square based on passed coordinates
                pygame.draw.circle(screen, CIRCLE_COLOUR, (int(col * 100 + 50),
                                                           int(row * 100 + 50)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOUR, (col * 100 + SPACE, row * 100 + 100 - SPACE),
                                 (col * 100 + 100 - SPACE, row * 100 + SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOUR, (col * 100 + SPACE, row * 100 + SPACE),
                                 (col * 100 + 100 - SPACE, row * 100 + 100 - SPACE), X_WIDTH)


def mark_square(row, column, player):
    board[row][column] = player


def available_square(row, column):
    if board[row][column] == 0:
        return True
    else:
        return False


def is_board_full():
    for all_rows in range(BOARD_ROWS):
        for all_cols in range(BOARD_COLUMNS):
            if board[all_rows][all_cols] == 0:
                return False
    return True


def check_win(player):
    # Vertical win check
    for col in range(BOARD_COLUMNS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player:
                draw_vertical_winning_line(col, player, 15, 415)
                return True
            if board[1][col] == player and board[2][col] == player and board[3][col] == player and board[4][col] == player:
                draw_vertical_winning_line(col, player, 115, 315)
                return True
            if board[2][col] == player and board[3][col] == player and board[4][col] == player and board[5][col] == player:
                draw_vertical_winning_line(col, player, 215, 215)
                return True
            if board[3][col] == player and board[4][col] == player and board[5][col] == player and board[6][col] == player:
                draw_vertical_winning_line(col, player, 315, 115)
                return True
            if board[4][col] == player and board[5][col] == player and board[6][col] == player and board[7][col] == player:
                draw_vertical_winning_line(col, player, 415, 15)
                return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player and board[row][3] == player:
            draw_horizontal_winning_line(row, player, 15, 415)
            return True
        if board[row][1] == player and board[row][2] == player and board[row][3] == player and board[row][4] == player:
            draw_horizontal_winning_line(row, player, 115, 315)
            return True
        if board[row][2] == player and board[row][3] == player and board[row][4] == player and board[row][5] == player:
            draw_horizontal_winning_line(row, player, 215, 215)
            return True
        if board[row][3] == player and board[row][4] == player and board[row][5] == player and board[row][6] == player:
            draw_horizontal_winning_line(row, player, 315, 115)
            return True
        if board[row][4] == player and board[row][5] == player and board[row][6] == player and board[row][7] == player:
            draw_horizontal_winning_line(row, player, 415, 15)
            return True

    # DESC diagonal win check
        # DESC middle
        if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player:
            draw_diagonal_line(player, 15, 15, 415, 415)
            return True
        if board[1][1] == player and board[2][2] == player and board[3][3] == player and board[4][4] == player:
            draw_diagonal_line(player, 115, 115, 315, 315)
            return True
        if board[2][2] == player and board[3][3] == player and board[4][4] == player and board[5][5] == player:
            draw_diagonal_line(player, 215, 215, 215, 215)
            return True
        if board[3][3] == player and board[4][4] == player and board[5][5] == player and board[6][6] == player:
            draw_diagonal_line(player, 315, 315, 115, 115)
            return True
        if board[4][4] == player and board[5][5] == player and board[6][6] == player and board[7][7] == player:
            draw_diagonal_line(player, 415, 415, 15, 15)
            return True

        # DESC right
        if board[0][1] == player and board[1][2] == player and board[2][3] == player and board[3][4] == player:
            draw_diagonal_line(player, 115, 15, 315, 415)
            return True
        if board[1][2] == player and board[2][3] == player and board[3][4] == player and board[4][5] == player:
            draw_diagonal_line(player, 215, 115, 215, 315)
            return True
        if board[2][3] == player and board[3][4] == player and board[4][5] == player and board[5][6] == player:
            draw_diagonal_line(player, 315, 215, 115, 215)
            return True
        if board[3][4] == player and board[4][5] == player and board[5][6] == player and board[6][7] == player:
            draw_diagonal_line(player, 415, 315, 15, 115)
            return True

        if board[0][2] == player and board[1][3] == player and board[2][4] == player and board[3][5] == player:
            draw_diagonal_line(player, 215, 15, 215, 415)
            return True
        if board[1][3] == player and board[2][4] == player and board[3][5] == player and board[4][6] == player:
            draw_diagonal_line(player, 315, 115, 115, 315)
            return True
        if board[2][4] == player and board[3][5] == player and board[4][6] == player and board[5][7] == player:
            draw_diagonal_line(player, 415, 215, 15, 215)
            return True

        if board[0][3] == player and board[1][4] == player and board[2][5] == player and board[3][6] == player:
            draw_diagonal_line(player, 315, 15, 115, 415)
            return True
        if board[1][4] == player and board[2][5] == player and board[3][6] == player and board[4][7] == player:
            draw_diagonal_line(player, 415, 115, 15, 315)
            return True

        if board[0][4] == player and board[1][5] == player and board[2][6] == player and board[3][7] == player:
            draw_diagonal_line(player, 415, 15, 15, 415)
            return True

        # DESC left
        if board[1][0] == player and board[2][1] == player and board[3][2] == player and board[4][3] == player:
            draw_diagonal_line(player, 15, 115, 415, 315)
            return True
        if board[2][1] == player and board[3][2] == player and board[4][3] == player and board[5][4] == player:
            draw_diagonal_line(player, 115, 215, 315, 215)
            return True
        if board[3][2] == player and board[4][3] == player and board[5][4] == player and board[6][5] == player:
            draw_diagonal_line(player, 215, 315, 215, 115)
            return True
        if board[4][3] == player and board[5][4] == player and board[6][5] == player and board[7][6] == player:
            draw_diagonal_line(player, 315, 415, 115, 15)
            return True

        if board[2][0] == player and board[3][1] == player and board[4][2] == player and board[5][3] == player:
            draw_diagonal_line(player, 15, 215, 415, 215)
            return True
        if board[3][1] == player and board[4][2] == player and board[5][3] == player and board[6][4] == player:
            draw_diagonal_line(player, 115, 315, 315, 115)
            return True
        if board[4][2] == player and board[5][3] == player and board[6][4] == player and board[7][5] == player:
            draw_diagonal_line(player, 215, 415, 215, 15)
            return True

        if board[3][0] == player and board[4][1] == player and board[5][2] == player and board[6][3] == player:
            draw_diagonal_line(player, 15, 315, 415, 115)
            return True
        if board[4][1] == player and board[5][2] == player and board[6][3] == player and board[7][4] == player:
            draw_diagonal_line(player, 115, 415, 315, 15)
            return True

        if board[4][0] == player and board[5][1] == player and board[6][2] == player and board[7][3] == player:
            draw_diagonal_line(player, 15, 415, 415, 15)
            return True

# ASC diagonal win check
    # ASC middle
        if board[7][0] == player and board[6][1] == player and board[5][2] == player and board[4][3] == player:
            draw_diagonal_line(player, 15, 785, 415, 385)
            return True
        if board[6][1] == player and board[5][2] == player and board[4][3] == player and board[3][4] == player:
            draw_diagonal_line(player, 115, 685, 315, 485)
            return True
        if board[5][2] == player and board[4][3] == player and board[3][4] == player and board[2][5] == player:
            draw_diagonal_line(player, 215, 585, 215, 585)
            return True
        if board[4][3] == player and board[3][4] == player and board[2][5] == player and board[1][6] == player:
            draw_diagonal_line(player, 315, 485, 115, 685)
            return True
        if board[3][4] == player and board[2][5] == player and board[1][6] == player and board[0][7] == player:
            draw_diagonal_line(player, 415, 385, 15, 785)
            return True

        # ASC left
        if board[6][0] == player and board[5][1] == player and board[4][2] == player and board[3][3] == player:
            draw_diagonal_line(player, 15, 685, 415, 485)
            return True
        if board[5][1] == player and board[4][2] == player and board[3][3] == player and board[2][4] == player:
            draw_diagonal_line(player, 115, 585, 315, 585)
            return True
        if board[4][2] == player and board[3][3] == player and board[2][4] == player and board[1][5] == player:
            draw_diagonal_line(player, 215, 485, 215, 685)
            return True
        if board[3][3] == player and board[2][4] == player and board[1][5] == player and board[0][6] == player:
            draw_diagonal_line(player, 315, 385, 115, 785)
            return True

        if board[5][0] == player and board[4][1] == player and board[3][2] == player and board[2][3] == player:
            draw_diagonal_line(player, 15, 585, 415, 585)
            return True
        if board[4][1] == player and board[3][2] == player and board[2][3] == player and board[1][4] == player:
            draw_diagonal_line(player, 115, 485, 315, 685)
            return True
        if board[3][2] == player and board[2][3] == player and board[1][4] == player and board[0][5] == player:
            draw_diagonal_line(player, 215, 385, 215, 785)
            return True

        if board[4][0] == player and board[3][1] == player and board[2][2] == player and board[1][3] == player:
            draw_diagonal_line(player, 15, 485, 415, 685)
            return True
        if board[3][1] == player and board[2][2] == player and board[1][3] == player and board[0][4] == player:
            draw_diagonal_line(player, 115, 385, 315, 785)
            return True

        if board[3][0] == player and board[2][1] == player and board[1][2] == player and board[0][3] == player:
            draw_diagonal_line(player, 15, 385, 415, 785)
            return True

        # # ASC right
        if board[7][1] == player and board[6][2] == player and board[5][3] == player and board[4][4] == player:
            draw_diagonal_line(player, 115, 785, 315, 385)
            return True
        if board[6][2] == player and board[5][3] == player and board[4][4] == player and board[3][5] == player:
            draw_diagonal_line(player, 215, 685, 215, 485)
            return True
        if board[5][3] == player and board[4][4] == player and board[3][5] == player and board[2][6] == player:
            draw_diagonal_line(player, 315, 585, 115, 585)
            return True
        if board[4][4] == player and board[3][5] == player and board[2][6] == player and board[1][7] == player:
            draw_diagonal_line(player, 415, 485, 15, 685)
            return True

        if board[7][2] == player and board[6][3] == player and board[5][4] == player and board[4][5] == player:
            draw_diagonal_line(player, 215, 785, 215, 385)
            return True
        if board[6][3] == player and board[5][4] == player and board[4][5] == player and board[3][6] == player:
            draw_diagonal_line(player, 315, 685, 115, 485)
            return True
        if board[5][4] == player and board[4][5] == player and board[3][6] == player and board[2][7] == player:
            draw_diagonal_line(player, 415, 585, 15, 585)
            return True

        if board[7][3] == player and board[6][4] == player and board[5][5] == player and board[4][6] == player:
            draw_diagonal_line(player, 315, 785, 115, 385)
            return True
        if board[6][4] == player and board[5][5] == player and board[4][6] == player and board[3][7] == player:
            draw_diagonal_line(player, 415, 685, 15, 485)
            return True

        if board[7][4] == player and board[6][5] == player and board[5][6] == player and board[4][7] == player:
            draw_diagonal_line(player, 415, 785, 15, 385)
            return True

    return False


def draw_vertical_winning_line(col, player, pos_1, pos_2):
    pos_y = col * 100 + 50

    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = X_COLOUR

    pygame.draw.line(screen, colour, (pos_y, pos_1), (pos_y, HEIGHT - pos_2), 10)


def draw_horizontal_winning_line(row, player, pos_1, pos_2):
    pos_x = row * 100 + 50

    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = X_COLOUR

    pygame.draw.line(screen, colour, (pos_1, pos_x), (WIDTH - pos_2, pos_x), 10)


def draw_diagonal_line(player, pos_1, pos_2, pos_3, pos_4):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = X_COLOUR

    pygame.draw.line(screen, colour, (pos_1, pos_2), (WIDTH - pos_3, HEIGHT - pos_4), 10)


def restart_game():
    screen.fill(BG_COLOUR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseY = event.pos[1]
            mouseX = event.pos[0]

            clicked_row = int(mouseY // 100)
            clicked_col = int(mouseX // 100)

            if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        if check_win(player):
                            font = pygame.font.SysFont('calibri.ttf', 28 )
                            text = """Congratulations Player 1! You win! Player 2, you SUCK! Press "r" to play again"""
                            img = font.render(text, True, TEXT_COLOUR)
                            screen.blit(img, (20, 20))
                            game_over = True
                        player = 2
                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        if check_win(player):
                            font = pygame.font.SysFont('calibri.ttf', 28)
                            text = """Congratulations Player 2! You win! Player 1, you SUCK! Press "r" to play again"""
                            img = font.render(text, True, TEXT_COLOUR)
                            screen.blit(img, (20, 20))
                            game_over = True
                        player = 1

                    draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                restart_game()

    pygame.display.update()





