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
