from dataclasses import dataclass

@dataclass
class Edge:
    u: int # "From" vertex
    v: int # "To" vertex

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f'{self.u} -> {self.v}'
