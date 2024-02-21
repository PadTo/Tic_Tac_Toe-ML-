import sys
import pygame
import numpy as np
from Constants import *
import random as rand

pygame.init()
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tic Tac Toe (AI)")
screen.fill(BG_COLOR)


class Board:
    def __init__(self):
        self.squares = np.zeros((n, n))

    def final_state(self):
        '''
            Return 0 if there is no win yet
            Return 1 if player 1 wins
            Return 2 if player 2 wins
        '''

        # Horizontal wins
        for row in range(n):
            if (P1_SUM == np.sum(self.squares[row, :]) or P2_SUM == np.sum(self.squares[row, :])) and np.min(self.squares[row, :]) != 0:
                return self.squares[row, 0]

        # Vertical wins
        for col in range(n):
            if (P1_SUM == np.sum(self.squares[:, col]) or P2_SUM == np.sum(self.squares[:, col])) and np.min(self.squares[:, col]) != 0:
                return self.squares[row, 0]

        # Diagonal Wins
        # From the lower left to the upper right diagonal #
        if self.squares[0, 0] == self.squares[1, 1] == self.squares[2, 2] != 0:
            return self.squares[0, 0]

        # From the upper left to the lower right diagonal #
        if self.squares[2, 0] == self.squares[1, 1] == self.squares[2, 0] != 0:
            return self.squares[2, 0]

        return 0

    def get_empty_squares(self):
        empty_squares = []
        for row in range(n):
            for col in range(n):
                if self.check_if_empty(row, col):
                    empty_squares.append((row, col))

        return empty_squares

    def check_if_empty(self, row, col):
        return self.squares[row, col] == 0

    def mark_square(self, row, col, player):
        self.squares[row, col] = player


class Game:

    # Player 1: X
    # Player 2: O

    def __init__(self):
        self.board = Board()
        self.show_lines()
        self.current_player = 1
        self.players = (1, 2)
        self.game_mode = "AI"  # Or AI
        self.runing = True
        self.ai = AI()

    def show_lines(self):

        for i in range(1, n):
            pygame.draw.line(screen, BOARD_LINE_COLOR,
                             (OFFSET_BOARD_LINES, i * THIRD_OF_HEIGHT),
                             (WIDTH - OFFSET_BOARD_LINES, i * THIRD_OF_HEIGHT),
                             (BOARD_LINE_THICKNESS))

            pygame.draw.line(screen, BOARD_LINE_COLOR,
                             (i * THIRD_OF_WIDTH, OFFSET_BOARD_LINES),
                             (i * THIRD_OF_WIDTH, HEIGHT - OFFSET_BOARD_LINES),
                             (BOARD_LINE_THICKNESS))

    def draw_figures(self, row, col, player):

        # Player 1: X's
        # Player 2: O's

        # DRAWING X
        if player == 1:
            pygame.draw.line(screen, GRAY_X,
                             (THIRD_OF_WIDTH * col + OFFSET_X_AND_O,
                              THIRD_OF_HEIGHT * row + OFFSET_X_AND_O),
                             (THIRD_OF_WIDTH * col + THIRD_OF_WIDTH - OFFSET_X_AND_O,
                              THIRD_OF_HEIGHT * row + THIRD_OF_HEIGHT - OFFSET_X_AND_O),
                             (X_O_THICK))

            pygame.draw.line(screen, GRAY_X,
                             (THIRD_OF_WIDTH * col + THIRD_OF_WIDTH - OFFSET_X_AND_O,
                              THIRD_OF_HEIGHT * row + OFFSET_X_AND_O),
                             (THIRD_OF_WIDTH * col + OFFSET_X_AND_O,
                              THIRD_OF_HEIGHT * row + THIRD_OF_HEIGHT - OFFSET_X_AND_O),
                             (X_O_THICK))

        # DRAWING O
        else:
            pygame.draw.circle(screen, BEIGE_O,
                               (THIRD_OF_WIDTH // 2 + THIRD_OF_WIDTH * col,
                                THIRD_OF_HEIGHT // 2 + THIRD_OF_HEIGHT * row),
                               (THIRD_OF_HEIGHT - OFFSET_X_AND_O * 2) // 2, X_O_THICK)


class AI:

    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_square = board.get_empty_squares()
        idx = rand.randrange(0, len(empty_square))

        return empty_square[idx]  # [row, col]

    def eval(self, main_board):
        if self.level == 0:
            move = self.rnd(main_board)
        else:
            move = self.rnd(main_board)

        return move


def main():
    game = Game()
    board = game.board
    ai = game.ai
    # Main Loop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // THIRD_OF_HEIGHT
                col = pos[0] // THIRD_OF_WIDTH
                # print(row, col)

                if board.check_if_empty(row, col):

                    board.mark_square(row, col, game.current_player)
                    game.draw_figures(row, col, game.current_player)
                    # print(board.final_state())

                    game.current_player = 1 if game.current_player == 2 else 2

        if game.game_mode == "AI" and game.current_player == ai.player:
            pygame.display.update()

            row, col = ai.eval(board)
            board.mark_square(row, col, game.current_player)
            game.draw_figures(row, col, game.current_player)
            game.current_player = 1 if game.current_player == 2 else 2

        pygame.display.update()


main()
