from abc import ABC, abstractmethod

class Piece:
    @property
    def opposite(self):
        raise NotImplementedError('Should be implemented by subclasses')

class Board(ABC):
    @property
    @abstractmethod
    def turn(self):
        ...

    @abstractmethod
    def move(self, location):
        ...

    @property
    @abstractmethod
    def legal_moves(self):
        ...

    @property
    @abstractmethod
    def is_won(self):
        ...

    @property
    def is_drawn(self):
        return not self.is_won and len(self.legal_moves) == 0

    @abstractmethod
    def evaluate(self, player):
        ...
