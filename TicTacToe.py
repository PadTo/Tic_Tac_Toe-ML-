import sys
import pygame
import numpy as np
from Constants import *
import random as rand
import copy

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
                return self.squares[0, col]

        # Diagonal Wins
        # From the upper left to the lower right diagonal #
        if self.squares[0, 0] == self.squares[1, 1] == self.squares[2, 2] != 0:
            return self.squares[0, 0]

        # From the lower left to the upper right diagonal #
        if self.squares[2, 0] == self.squares[1, 1] == self.squares[0, 2] != 0:
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

    def is_full(self):
        for row in range(0, n):
            for col in range(0, n):
                if self.squares[row, col] == 0:
                    return False

        return True

    def reset_board(self):
        self.squares = np.zeros((n, n))


class Game:

    # Player 1: X
    # Player 2: O

    def __init__(self):
        self.board = Board()
        self.show_lines()
        self.current_player = 1
        self.players = [1, 2]
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

    def restart(self):

        self.game_mode = "AI"
        pygame.init()
        SCREEN_SIZE = (WIDTH, HEIGHT)
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Tic Tac Toe (AI)")
        screen.fill(BG_COLOR)
        self.show_lines()
        self.board.reset_board()

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

    def __init__(self, level=1, player=2):
        self.level = level  # level 0: Random, level 1: Min Max
        self.player = player

    def rnd(self, board):
        empty_square = board.get_empty_squares()
        idx = rand.randrange(0, len(empty_square))
        rand_eval = "Random"

        return rand_eval, empty_square[idx]  # [row, col]

    def minimax(self, board, maximizing):
        case = board.final_state()

        if case == 1:
            return -1, None

        if case == 2:
            return 1, None

        elif board.is_full():
            return 0, None

        if maximizing:
            best_move = None
            max_eval = -100

            for (row, col) in board.get_empty_squares():

                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval, _ = self.minimax(temp_board, False)

                if max_eval < eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        if not maximizing:  # Minimizing
            best_move = None
            min_eval = 100

            for (row, col) in board.get_empty_squares():

                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval, _ = self.minimax(temp_board, True)

                if min_eval > eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            eval, move = self.rnd(main_board)
        else:
            eval, move = self.minimax(main_board, True)

        print(f"{eval}")

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.restart()

                if event.key == pygame.K_a:
                    game.game_mode = "AI"

                if event.key == pygame.K_p:
                    game.game_mode = "PvP"

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
            if board.is_full():
                pass

            else:
                row, col = ai.eval(board)
                board.mark_square(row, col, game.current_player)
                game.draw_figures(row, col, game.current_player)
                game.current_player = 1 if game.current_player == 2 else 2

        pygame.display.update()


main()
