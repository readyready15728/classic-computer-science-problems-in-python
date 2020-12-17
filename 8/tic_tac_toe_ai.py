from board import Board
from minimax import find_best_move
from tic_tac_toe import TicTacToeBoard

board = TicTacToeBoard()

def get_player_move():
    player_move = -1

    while player_move not in board.legal_moves:
        player_move = int(input('Enter a legal square (0-8):'))

    return player_move

if __name__ == '__main__':
    # Main game loop
    while True:
        human_move = get_player_move()
        board = board.move(human_move)

        if board.is_won:
            print('Human wins!')
            break
        elif board.is_drawn:
            print('Draw!')
            break

        computer_move = find_best_move(board)
        print(f'Computer move is {computer_move}')
        board = board.move(computer_move)
        print(board)

        if board.is_won:
            print('Computer wins!')
            break
        elif board.is_drawn:
            print('Draw!')
            break
