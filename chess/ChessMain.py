import pygame as p
from chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}
COLOR = "WHITE"


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color(COLOR))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMades = False

    loadImages()
    running = True
    sqSelected = ()
    playerClicked = []
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                row, col = location[1] // SQ_SIZE, location[0] // SQ_SIZE
                if sqSelected == (row, col):  # bỏ ô đã chọn
                    sqSelected = ()
                    playerClicked = []
                else:  # chọn một ô
                    sqSelected = (row, col)
                    playerClicked.append(sqSelected)
                if len(playerClicked) == 2:
                    move = ChessEngine.Move(playerClicked[0], playerClicked[1], gs.board)
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMades = True
                    sqSelected = ()
                    playerClicked = []
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    gs.undoMove()
                    moveMades = True
        if moveMades:
            validMoves = gs.getValidMoves()
            moveMades = False

        drawBoardState(screen, gs.board)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoardState(screen, board):
    drawBoard(screen)
    drawPieces(screen, board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)),


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
