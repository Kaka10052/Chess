from Figure import *


class Rook(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'rook'
        self.is_moved = False

    def availableMoves(self, chessboard, king):
        moves, tmp_x, tmp_y = [], self.x - 1, self.y
        # Left
        while tmp_x >= 0:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x -= 1
        # Right
        tmp_x = self.x + 1
        while tmp_x <= 7:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x += 1
        # Up
        tmp_x, tmp_y = self.x, self.y + 1
        while tmp_y <= 7:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_y += 1
        # Down
        tmp_y = self.y - 1
        while tmp_y >= 0:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_y -= 1
        moves = self.moves_without_check(chessboard, moves, king)
        return moves
