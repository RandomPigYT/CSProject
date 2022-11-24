from chess import globals as g
from chess import generateMoves as gm

def attackedSquares(colour) -> list:
    pieces = []
    
    g.attacked = []

    if colour == g.Piece.white:
        pieces = g.whitePieceLocations

    else:
        pieces = g.blackPieceLocations


    for i in pieces:
        if g.board[i] == g.Piece.Pawn:
            g.attacked.extend(gm.pawnAttacks(g.board[i], i))
            continue


        elif g.board[i] != g.Piece.King:
            g.attacked.extend(gm.generateMoves((g.board[i], i)))

