####### Constants for the board heigh, width, colors, and thickness #######

HEIGHT = 600
WIDTH = 600
n = 3  # The square size (n x n) of the traditional tic-tac-toe game

# Calculating the square dimensions of the board
THIRD_OF_HEIGHT = HEIGHT // n
THIRD_OF_WIDTH = WIDTH // n

BOARD_LINE_THICKNESS = THIRD_OF_WIDTH // 15
X_O_THICK = WIDTH // 50
WINNING_LINE_THICK = WIDTH // 55


# Note that n can be later changed to analyze if the game works
# with a bigger square size

# Calculating the square dimensions of the board
THIRD_OF_HEIGHT = HEIGHT // n
THIRD_OF_WIDTH = WIDTH // n

# Initializing some RGB Colors
BEIGE_O = (242, 235, 211)  # Color of O's
GRAY_X = (85, 85, 85)      # Color of X's
BG_COLOR = (20, 189, 172)  # Color of the background
BOARD_LINE_COLOR = (13, 161, 146)  # Color of the board lines
BLACK = (0, 0, 0)


# Offsets for different lines (drawing) __Scaling__
OFFSET_X_AND_O = THIRD_OF_WIDTH // 5
OFFSET_BOARD_LINES = HEIGHT // 40
OFFSET_WINNING_LINES = HEIGHT // 50


# Values to see if the rows or columns accumulate to the winning sum
# Player 1 winning sum: 3
# Player 2 winning sum: 6

P1_SUM = 3
P2_SUM = 6
