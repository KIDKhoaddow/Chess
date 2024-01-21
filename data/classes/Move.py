import copy


class Move:
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = copy.copy(board.get_piece_from_pos((self.startRow, self.startCol)))
        self.pieceCaptured = copy.copy(board.get_piece_from_pos((self.endRow, self.endCol)))
        self.moveId = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False
