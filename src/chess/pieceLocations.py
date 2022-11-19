from chess import globals as g


def pieceLocations():
    
    g.whitePieceLocations = []
    g.blackPieceLocations = []

    for i in range(len(g.board)):

        square = g.board[i]

        # Check if the square has a piece
        if square:
            if square & 0b11000 == g.Piece.white:
                g.whitePieceLocations.append(i)

            else:
                g.blackPieceLocations.append(i)
