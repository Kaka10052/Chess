from Figure import *
from Queen import *
from Knight import *


class Pawn(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'pawn'
        self.is_moved = False
        self.en_passant = False

    def promotion(self, to_x, to_y):
        if (to_y == 7 and self.color == 'white') or \
                (to_y == 0 and self.color == 'black'):
            which_figure = ''
            while which_figure not in figures or \
                  which_figure in ('king', 'pawn'):
                which_figure = input(
                    'Which figure do you want to get?')
            return eval(which_figure.capitalize())(
                to_x, to_y, self.color)

    def doing_en_passant(self, to_x, to_y, chessboard, window):
        if self.color == 'white':
            pawn = chessboard[to_x][to_y-1]
        else:
            pawn = chessboard[to_x][to_y+1]
        if window:
            pawn.undraw()
        chessboard[pawn.x][pawn.y] = 0

    def availableMoves(self, chessboard, king):
        x, y = self.getCoords()
        moves, right_edge, left_edge = [], False, False
        if x == 7: right_edge = True
        if x == 0: left_edge = True
        # white pawn always moves upward and ...
        if self.color == 'white': operator = '+'
        # ... black pawn always moves downward
        else: operator = '-'
        tmp_y = eval('y'+operator+'1')
        if not right_edge and chessboard[x+1][tmp_y]:
            figure = chessboard[x + 1][tmp_y]
            if figure.color != self.color:
                moves.append((x + 1, tmp_y))
        if not left_edge and chessboard[x-1][tmp_y]:
            figure = chessboard[x-1][tmp_y]
            if figure.color != self.color:
                moves.append((x - 1, tmp_y))
        if not chessboard[x][tmp_y]:
            moves.append((x, tmp_y))
            tmp_y = eval('y'+operator+'2')
            if not self.is_moved and not chessboard[x][tmp_y]:
                moves.append((x, tmp_y))
        if self.en_passant:
            moves.append(self.en_passant)
        return self.moves_without_check(chessboard, moves, king)

    def move(self, to_x, to_y, chessboard,
             opp_king=False, window=False):
        is_promoted = False
        # promotion of a pawn
        if to_y in (0, 7) and window:
            is_promoted = True
            new_figure = self.promotion(to_x, to_y)
            opp_king.replace_piece(self, new_figure)
            self.undraw()
            chessboard[to_x][to_y] = new_figure
            new_figure.draw(window)
        if not self.is_moved and window:
            self.is_moved = True
            # make en passant available
            if abs(to_y - self.y) == 2:
                if self.color == 'white':
                    en_passant_y = self.y+1
                else:
                    en_passant_y = self.y-1
                if to_x-1 >= 0 and \
                        isinstance(chessboard[to_x - 1][to_y], Figure) and \
                        chessboard[to_x-1][to_y].name == 'pawn' and \
                        chessboard[to_x-1][to_y].color != self.color:
                    other = chessboard[to_x-1][to_y]
                    other.en_passant = (to_x, en_passant_y)
                elif to_x + 1 <= 7 and \
                        isinstance(chessboard[to_x + 1][to_y], Figure) and \
                        chessboard[to_x + 1][to_y].name == 'pawn' and \
                        chessboard[to_x + 1][to_y].color != self.color:
                    other = chessboard[to_x + 1][to_y]
                    other.en_passant = (to_x, en_passant_y)
        self.setCoords(to_x, to_y)
        if window and not is_promoted:
            self.undraw()
            self.draw(window)

    def moving_piece(self, to_x, to_y, chessboard,
                     opp_king=False, window=False):
        Figure.moving_piece(self, to_x, to_y, chessboard,
                            opp_king=opp_king, window=window)
        if (to_x, to_y) == self.en_passant and window:
            self.doing_en_passant(to_x, to_y, chessboard, window)

