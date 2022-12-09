import pygame
from window import window as w
from chess import globals as g
from chess import util
from sprites import sprites as s


def getPieceName(pieceVal):
    name = ""

    piece: g.Piece = g.Piece()

    colour = lambda val: "black" if val == 16 else "white"
    pieces = {
        piece.King: "King",
        piece.Pawn: "Pawn",
        piece.Knight: "Knight",
        piece.Bishop: "Bishop",
        piece.Rook: "Rook",
        piece.Queen: "Queen",
    }

    name = colour(pieceVal & g.colourMask) + pieces[pieceVal & g.pieceMask] + ".png"

    return name


def drawPieces(window: w.PygameWindow):

    # sSheet = s.SpriteSheet("assets/piece_sprites.png")
    sprite = None

    for i in range(len(g.board)):
        if g.board[i] != 0:
            sprite = pygame.transform.scale(
                g.sSheet.GetSprite(getPieceName(g.board[i]), 256, 256), (g.side, g.side)
            )

            window.screen.blit(
                sprite,
                (
                    g.squareCentres[i][0] - (g.side / 2),
                    g.squareCentres[i][1] - (g.side / 2),
                ),
            )

    if len(g.heldPiece) != 0 and g.heldPiece[0] != 0:
        mousePos = pygame.mouse.get_pos()

        sprite = pygame.transform.scale(
            g.sSheet.GetSprite(getPieceName(g.heldPiece[0]), 256, 256), (g.side, g.side)
        )
        window.screen.blit(
            sprite, (mousePos[0] - (g.side / 2), mousePos[1] - (g.side / 2))
        )


def getSquareCentres(startPos, offset):

    calculateCentres = lambda squarePos, side: (
        squarePos[0] + (side / 2),
        squarePos[1] + (side / 2),
    )

    rank: int = 0
    while rank < 8:
        file: int = 0
        while file < 8:

            g.squareCentres[util.coordsToIndex(7 - rank, file)] = calculateCentres(
                (startPos[0] + (file * g.side), offset + (rank * g.side)), g.side
            )

            file += 1
        rank += 1


def drawBoard(window: w.PygameWindow):

    window.screen.fill((49, 46, 43))

    white: tuple = (240, 218, 181)
    black: tuple = (181, 135, 99)

    g.size = pygame.display.get_surface().get_size()

    # Math!
    offset: float = (g.size[1] - (g.weight * g.size[1])) / 2

    size: float = pygame.display.get_surface().get_size()
    boardSize: float = g.size[1] * g.weight
    side: int = boardSize / 8
    startPos: tuple = ((g.size[0] - g.boardSize) / 2, offset)

    g.boardSize = boardSize
    g.side = side

    # find the centres of the squares
    g.boardImage = pygame.transform.scale(g.imageCopy, (boardSize, boardSize))

    getSquareCentres(startPos, offset)

    # draw board
    window.screen.blit(g.boardImage, startPos)
    g.prevSize = size
