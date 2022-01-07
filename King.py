from Figure import *
from Pawn import *


class King(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'king'
        self.is_moved = False
        self.check_checks = True
        self.opponent_pieces = []

    def setOpponentPieces(self, pieces):
        self.opponent_pieces = pieces

    def check(self, chessboard):
        if self.check_checks:
            opponent_king = self.opponent_pieces[8]
            opponent_king.check_checks = False
            for piece in self.opponent_pieces:
                if (self.x, self.y) in piece.availableMoves(
                        chessboard, opponent_king) \
                        and any(piece in _ for _ in chessboard):
                    return True
        return False

    def castle_moves(self, moves, chessboard):
        if not self.is_moved:
            king_side = not chessboard[self.x + 1][self.y] and \
                        not chessboard[self.x + 2][self.y] and \
                        (self.x + 1, self.y) in moves and \
                        chessboard[self.x + 3][self.y] and \
                        not chessboard[self.x + 3][self.y].is_moved
            queen_side = not chessboard[self.x - 1][self.y] and \
                         not chessboard[self.x - 2][self.y] and \
                         not chessboard[self.x - 3][self.y] and \
                         (self.x - 1, self.y) in moves and \
                         chessboard[self.x - 4][self.y] and \
                         not chessboard[self.x - 4][self.y].is_moved
            if king_side:
                moves.append((self.x + 2, self.y))
            if queen_side:
                moves.append((self.x - 2, self.y))

    def availableMoves(self, chessboard, king):
        tmp_moves, x, y = [], self.x, self.y
        all_moves = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                     (x, y - 1),                 (x, y + 1),
                     (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        for move in all_moves:
            tmp_x, tmp_y = move
            if 0 <= tmp_x <= 7 and 0 <= tmp_y <= 7:
                if chessboard[tmp_x][tmp_y]:
                    figure = chessboard[tmp_x][tmp_y]
                    if figure.color != self.color:
                        tmp_moves.append(move)
                else:
                    tmp_moves.append(move)
        if not self.check(chessboard):
            self.castle_moves(tmp_moves, chessboard)
        moves = self.moves_without_check(chessboard,
                                         tmp_moves, king)
        if (self.x + 2, self.y) in moves \
                and not (self.x + 1, self.y) in moves:
            del moves[moves.index((self.x + 2, self.y))]
        if (self.x - 2, self.y) in moves \
                and not (self.x - 1, self.y) in moves:
            del moves[moves.index((self.x - 2, self.y))]
        return moves

    def castling(self, to_x, chessboard, window=False):
        x, y = self.x, self.y
        if not self.is_moved and abs(x - to_x) == 2 and window:
            # short castle
            if to_x > x:
                rook = chessboard[7][y]
                old_x, old_y = rook.getCoords()
                rook.move(5, y, chessboard, window=window)
                rook, chessboard[5][y] = \
                    chessboard[5][y], rook
                chessboard[old_x][old_y] = 0
            # long castle
            else:
                rook = chessboard[0][y]
                old_x, old_y = rook.getCoords()
                rook.move(3, y, chessboard, window=window)
                rook, chessboard[3][y] = \
                    chessboard[3][y], rook
                chessboard[old_x][old_y] = 0

    def moving_piece(self, to_x, to_y, chessboard,
                     opp_king=False, window=False):
        Figure.moving_piece(self, to_x, to_y, chessboard,
                            opp_king=opp_king, window=window)
        self.castling(to_x, chessboard, window)

    def disable_old_en_passant(self):
        for piece in self.opponent_pieces:
            if isinstance(piece, Pawn) and piece.en_passant:
                piece.en_passant = False

    def replace_piece(self, to_replace, replacer):
        for i, piece in enumerate(self.opponent_pieces):
            if to_replace == piece:
                if replacer == 0:
                    del self.opponent_pieces[i]
                else:
                    self.opponent_pieces[i] = replacer
                break
