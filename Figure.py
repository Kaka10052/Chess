from pathlib import Path
from graphics import *
from abc import ABC

figures = {
    'king': 'K',
    'queen': 'Q',
    'knight': 'N',
    'bishop': 'B',
    'pawn': 'P',
    'rook': 'R'
}
colors = {
    'white': 'W',
    'black': 'B'
}


class Figure(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = 'default'
        self.image = ''

    def __repr__(self):
        return f'(Figure: x={self.x}, y={self.y},' \
               f' color={self.color}, name={self.name})'

    def __str__(self):
        return colors[self.color]+figures[self.name]

    def draw(self, window):
        file_path = Path('images/') / self.color / (self.name + '.png')
        self.image = Image(Point(self.x + 0.5, self.y + 0.5), file_path)
        self.image.draw(window)

    def undraw(self):
        self.image.undraw()

    def getCoords(self):
        return self.x, self.y

    def getColor(self):
        return self.color

    def setCoords(self, to_x, to_y):
        self.x = to_x
        self.y = to_y

    def availableMoves(self, chessboard, king):
        pass

    def move(self, to_x, to_y, chessboard,
             opp_king=False, window=False):
        if hasattr(self, 'is_moved') and window:
            self.is_moved = True
        self.setCoords(to_x, to_y)
        if window:
            self.undraw()
            self.draw(window)

    def capture(self, other, chessboard,
                opp_king=False, window=False):
        if window:
            other.undraw()
        chessboard[self.x][self.y], chessboard[other.x][other.y] = \
            0, chessboard[self.x][self.y]
        self.move(other.x, other.y, chessboard, opp_king, window)

    def moving_piece(self, to_x, to_y, chessboard,
                     opp_king=False, window=False):
        x, y = self.getCoords()
        if isinstance(chessboard[to_x][to_y], Figure):
            other = chessboard[to_x][to_y]
            self.capture(other, chessboard, opp_king, window)
        else:
            self.move(to_x, to_y, chessboard, opp_king, window)
            chessboard[x][y], chessboard[to_x][to_y] = \
                chessboard[to_x][to_y], chessboard[x][y]

    def moves_without_check(self, chessboard, tmp_moves, my_king):
        if my_king.check_checks:
            moves = []
            for (to_x, to_y) in tmp_moves:
                x, y = self.getCoords()
                tmp_1, tmp_2 = chessboard[x][y], chessboard[to_x][to_y]
                self.moving_piece(to_x, to_y, chessboard)
                if not my_king.check(chessboard):
                    moves.append((to_x, to_y))
                self.setCoords(x, y)
                chessboard[x][y] = tmp_1
                chessboard[to_x][to_y] = tmp_2
            return moves
        return tmp_moves
