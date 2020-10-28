import math
import random
from collections import namedtuple
from generic_search import dfs, bfs, node_to_path, a_star, Node

class Cell:
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'

MazeLocation = namedtuple('MazeLocation', ['row', 'column'])
