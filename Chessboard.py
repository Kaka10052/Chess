from Pawn import *
from Queen import *
from Knight import *
from King import *


def visualization_of_chessboard():
    window = GraphWin('Szachy', 400, 400)
    window.setBackground('white')
    window.setCoords(0, 0, 8, 8)
    # Drawing lines that seperate squares
    for i in range(9):
        line1 = Line(Point(0, i), Point(8, i))
        line2 = Line(Point(i, 0), Point(i, 8))
        line1.draw(window)
        line2.draw(window)
    # Drawing grey squares
    for x in range(8):
        for y in range(4):
            square = Rectangle(Point(x, 2 * y + x % 2),
                               Point(x + 1, 2 * y + 1 + x % 2))
            square.setFill('grey')
            square.draw(window)
            del square
    return window


def draw_chessboard(chessboard):
    chessboard_t = list(zip(*chessboard))
    for x in range(7, -1, -1):
        for y in range(8):
            print(chessboard_t[x][y], end=" ")
            if chessboard_t[x][y] == 0:
                print(end=' ')
        print()
    print()


def starting_chessboard(window):
    chessboard = [[0 for _ in range(8)] for _ in range(8)]
    # Pawns
    for x in range(8):
        chessboard[x][1] = Pawn(x, 1, 'white')
        chessboard[x][6] = Pawn(x, 6, 'black')
    # Bishops
    chessboard[2][0] = Bishop(2, 0, 'white')
    chessboard[5][0] = Bishop(5, 0, 'white')
    chessboard[2][7] = Bishop(2, 7, 'black')
    chessboard[5][7] = Bishop(5, 7, 'black')
    # Rooks
    chessboard[0][0] = Rook(0, 0, 'white')
    chessboard[7][0] = Rook(7, 0, 'white')
    chessboard[0][7] = Rook(0, 7, 'black')
    chessboard[7][7] = Rook(7, 7, 'black')
    # Knights
    chessboard[1][0] = Knight(1, 0, 'white')
    chessboard[6][0] = Knight(6, 0, 'white')
    chessboard[1][7] = Knight(1, 7, 'black')
    chessboard[6][7] = Knight(6, 7, 'black')
    # Queens
    chessboard[3][0] = Queen(3, 0, 'white')
    chessboard[3][7] = Queen(3, 7, 'black')
    # Kings
    chessboard[4][0] = King(4, 0, 'white')
    chessboard[4][7] = King(4, 7, 'black')
    for x in range(8):
        for y in (0, 1, 6, 7):
            chessboard[x][y].draw(window)
    return chessboard
