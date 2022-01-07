from Figure import *


class Knight(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'knight'

    def availableMoves(self, chessboard, king):
        moves, x, y = [], self.x, self.y
        all_moves = [(x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1),
                     (x-1, y-2), (x+1, y-2), (x-2, y+1), (x-2, y-1)]
        for move in all_moves:
            tmp_x, tmp_y = move
            if 0 <= tmp_x <= 7 and 0 <= tmp_y <= 7:
                if chessboard[tmp_x][tmp_y]:
                    figure = chessboard[tmp_x][tmp_y]
                    if figure.color != self.color:
                        moves.append(move)
                else:
                    moves.append(move)
        return self.moves_without_check(chessboard, moves, king)
