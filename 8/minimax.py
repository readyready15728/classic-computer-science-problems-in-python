from board import Board, Piece

def minimax(board, maximizing, original_player, max_depth=8):
    # Base case: terminal position or maximum depth reached
    if board.is_won or board.is_drawn or max_depth == 0:
        return board.evaluate(original_player)

    # Recursive case maximize your gains or minimize the opponent's gains
    if maximizing:
        best_evaluation = float('-inf')

        for move in board.legal_moves:
            result = minimax(board.move(move), False, original_player, max_depth - 1)
            best_evaluation = max(result, best_evaluation)

        return best_evaluation
    else:
        worst_evaluation = float('inf')

        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_evaluation = min(result, worst_evaluation)

        return worst_evaluation

def find_best_move(board, max_depth=8):
    best_evaluation = float('-inf')
    best_move = -1

    for move in board.legal_moves:
        result = minimax(board.move(move), False, board.turn, max_depth)

        if result > best_evaluation:
            best_evaluation = result
            best_move = move

    return best_move
