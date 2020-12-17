from board import Board, Move, Piece

class TicTacToePiece(Piece):
    X = 'X'
    O = 'O'
    E = ' '

    @property
    def opposite(self):
        if self == self.__class__.X:
            return self.__class__.O
        elif self == self.__class__.O:
            return self == self.__class__.X
        else:
            return self.__class__.E

    def __str__(self):
        return self.value

class TicTacToeBoard(Board):
    def __init__(self, position=[TicTacToePiece.E] * 9, turn=TicTacToePiece.X):
        self.position = position
        self._turn = turn

    @property
    def turn(self):
        return self._turn

    def move(self, location):
        temp_position = self.position.copy()
        temp_position[location] = self._turn

        return TicTacToeBoard(temp_position, self._turn.opposite)

    @property
    def legal_moves(self):
        return [Move(i) for i in range(len(self.position)) if self.position[i] == TicTacToePiece.E]

    @property
    def is_won(self):
        # Three row, three column, and then two diagonal checks
        return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TicTacToePiece.E or \
        self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != TicTacToePiece.E or \
        self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TicTacToePiece.E or \
        self.position[0] == self.position[3] and self.position[0] == self.position[6] and self.position[0] != TicTacToePiece.E or \
        self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TicTacToePiece.E or \
        self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != TicTacToePiece.E or \
        self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TicTacToePiece.E or \
        self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TicTacToePiece.E

    def evaluate(self, player):
        if self.is_won and self.turn == player:
            return -1
        elif self.is_won and self.turn != player:
            return 1
        else:
            return 0

    def __repr__(self):
        return f"""{self.position[0]}|{self.position[1]}|{self.position[2]}
-----
{self.position[3]}|{self.position[4]}|{self.position[5]}
-----
{self.position[6]}|{self.position[7]}|{self.position[8]}"""
