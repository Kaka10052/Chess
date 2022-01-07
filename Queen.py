from Figure import *
from Rook import *
from Bishop import *


class Queen(Rook, Bishop):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'queen'

    def availableMoves(self, chessboard, king):
        moves = [move for move in Rook.availableMoves(
            self, chessboard, king)]
        moves.extend([move for move in Bishop.availableMoves(
            self, chessboard, king)])
        return moves
