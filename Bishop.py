from Figure import *


class Bishop(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'bishop'

    def availableMoves(self, chessboard, king):
        moves, tmp_x, tmp_y = [], self.x-1, self.y+1
        # Up-left diagonal
        while tmp_x >= 0 and tmp_y <= 7:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x -= 1
            tmp_y += 1
        # Up-right diagonal
        tmp_x, tmp_y = self.x+1, self.y+1
        while tmp_x <= 7 and tmp_y <= 7:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x += 1
            tmp_y += 1
        # Down-left diagonal
        tmp_x, tmp_y = self.x - 1, self.y - 1
        while tmp_x >= 0 and tmp_y >= 0:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x -= 1
            tmp_y -= 1
        # Down-right diagonal
        tmp_x, tmp_y = self.x + 1, self.y - 1
        while tmp_x <= 7 and tmp_y >= 0:
            if chessboard[tmp_x][tmp_y]:
                figure = chessboard[tmp_x][tmp_y]
                if figure.color != self.color:
                    moves.append((tmp_x, tmp_y))
                break
            else:
                moves.append((tmp_x, tmp_y))
            tmp_x += 1
            tmp_y -= 1
        return self.moves_without_check(chessboard, moves, king)
