from Chessboard import *


def user_click_coords(window):
    user_click = window.getMouse()
    x = int(user_click.getX())
    if x == 8:
        x = 7
    y = int(user_click.getY())
    if y == 8:
        y = 7
    return x, y


def change_color(color):
    if color == 'white':
        return 'black'
    else:
        return 'white'


def draw_circles_of_moves(moves, window):
    circles_of_moves = []
    for i, (x, y) in enumerate(moves):
        circles_of_moves.append(
            Circle(Point(x + 0.5, y + 0.5), 0.25) )
        circles_of_moves[i].setFill('dark blue')
        circles_of_moves[i].draw(window)
    return circles_of_moves


window = visualization_of_chessboard()
chessboard = starting_chessboard(window)
black_pieces, white_pieces = [], []
for x in range(8):
    for y in (0, 1):
        white_pieces.append(chessboard[x][y])
    for y in (7, 6):
        black_pieces.append(chessboard[x][y])
black_king, white_king = chessboard[4][7], chessboard[4][0]
black_king.setOpponentPieces(white_pieces)
white_king.setOpponentPieces(black_pieces)

pointer_of_piece = Circle(Point(-1, -1), 0.5)
pointer_of_piece.setOutline('red')
pointer_of_piece.draw(window)
which_turn = 'white'
while True:
    draw_chessboard(chessboard)
    x, y = user_click_coords(window)
    pointer_of_piece.undraw()
    pointer_of_piece = Circle(Point(x+0.5, y+0.5), 0.5)
    pointer_of_piece.setOutline('red')
    if isinstance(chessboard[x][y], Figure):
        figure = chessboard[x][y]
        if figure.getColor() == which_turn:
            king = eval(which_turn + '_king')
            opponent_king = eval(change_color(which_turn) + '_king')
            king.check_checks = True
            king.disable_old_en_passant()
            av_moves = figure.availableMoves(chessboard, king)
            pointer_of_piece.draw(window)
            circles_of_moves = draw_circles_of_moves(av_moves, window)
            to_x, to_y = user_click_coords(window)
            for cir in circles_of_moves:
                cir.undraw()
                del cir
            pointer_of_piece.undraw()
            if (to_x, to_y) in av_moves:
                figure.moving_piece(to_x, to_y, chessboard,
                                    opponent_king, window)
                which_turn = change_color(which_turn)

# window.getMouse()
# window.close()
