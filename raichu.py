#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#Names - userID
#Sowmya Cheedu - scheedu
#Adarsha Reddy pedda gorla - adpeddag
#Vamsidhar pagadala - vpagada
#
# Based on skeleton code by D. Crandall, Oct 2021
import sys
import math
import random
import signal


def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def convert_index_to_row_and_column(index, board_size):
    row = index // board_size
    column = index % board_size
    return row, column

def convert_row_and_column_to_index(row, column, board_size):
    index = None
    if((row  in range(0, board_size)) and (column in range(0, board_size))):
        index = row * board_size + column
        return index
    return index

def is_last_row_check(index, board_size, player):

    if player == 'w' or player == 'W':
        row = index // board_size
        if (row == board_size -1):
            return True
        else:
            return False
    else :
        row = index // board_size
        if row == 0:
            return True
        else:
            return False

def is_opposite_color_piece_present(piece, target_piece):
    #print("piece value is: ", piece)
    #print("target piece is: ", target_piece.lower())
    if piece.lower() != target_piece.lower() and piece != '.' and target_piece != '.':
        return True
    else:
        return False

def pichu_moves(board, board_size, player, current_piece_index, player_pieces):
    current_row, current_column = convert_index_to_row_and_column(current_piece_index, board_size)
    #print("current piece: ", board[current_piece_index])
    piece_possible_moves = []

    bottom_row = 1
    if (player == 'b'):
        bottom_row = -1

    right_down = convert_row_and_column_to_index(current_row+1*bottom_row, current_column+1, board_size)
    left_down = convert_row_and_column_to_index(current_row+1*bottom_row, current_column-1, board_size)
    right_jump = convert_row_and_column_to_index(current_row+2*bottom_row, current_column+2, board_size)
    left_jump = convert_row_and_column_to_index(current_row+2*bottom_row, current_column-2, board_size)

    #right down valid move check and move to it
    if ((right_down is not None) and (board[right_down] == '.')) :
        new_board = list(board)
        #print("new board is : ", new_board)
        if (is_last_row_check(right_down, board_size, player)):
            new_board[right_down] = player_pieces[-1]
        else:
            new_board[right_down] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        #print("board after changing: ",''.join(new_board))
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})
        
    
    #left down valid move check and move to it
    if ((left_down is not None) and (board[left_down] == '.')) :
        new_board = list(board)
        if (is_last_row_check(left_down, board_size, player)):
            new_board[left_down] = player_pieces[-1]
        else:
            new_board[left_down] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        #print("board left down after changing: ",''.join(new_board))
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})
    
    #right jump valid move check and move to it
    if (right_jump is not None) and (board[right_jump] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[right_down])) and (str.islower(board[right_down])):
        #print("entered right jump")
        new_board = list(board)
        if (is_last_row_check(right_jump, board_size, player)):
            new_board[right_jump] = player_pieces[-1]
        else:
            new_board[right_jump] = board[current_piece_index]
        new_board[right_down] = '.'
        new_board[current_piece_index] = '.'
        #print("board right jump after changing: ",''.join(new_board))
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #left jump valid move check and move to it
    if (left_jump is not None) and (board[left_jump] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[left_down])) and (str.islower(board[left_down])):
        #print("entered left jump")
        new_board = list(board)
        if (is_last_row_check(left_jump, board_size, player)):
            new_board[left_jump] = player_pieces[-1]
        else:
            new_board[left_jump] = board[current_piece_index]
        new_board[left_down] = '.'
        new_board[current_piece_index] = '.'
        #print("board left jump after changing: ",''.join(new_board))
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #print("possible piece moves are : ", piece_possible_moves)
    return piece_possible_moves
def get_player_pieces(player: str):
    return "bB$" if player.lower() == "b" else "wW@"

def pikachu_moves(board, board_size, player, current_piece_index, player_pieces):
    current_row, current_column = convert_index_to_row_and_column(current_piece_index, board_size)
    #print("current piece: ", board[current_piece_index])
    piece_possible_moves = []

    bottom_row = 1
    if (player == 'B'):
        bottom_row = -1

    move_1_forward = convert_row_and_column_to_index(current_row+(1*bottom_row), current_column, board_size)
    move_2_forward = convert_row_and_column_to_index(current_row+(2*bottom_row), current_column, board_size)
    move_3_forward = convert_row_and_column_to_index(current_row+(3*bottom_row), current_column, board_size)
    move_1_left = convert_row_and_column_to_index(current_row, current_column-1, board_size)
    move_2_left = convert_row_and_column_to_index(current_row, current_column-2, board_size)
    move_3_left = convert_row_and_column_to_index(current_row, current_column-3, board_size)
    move_1_right = convert_row_and_column_to_index(current_row, current_column+1, board_size)
    move_2_right = convert_row_and_column_to_index(current_row, current_column+2, board_size)
    move_3_right = convert_row_and_column_to_index(current_row, current_column+3, board_size)


    #1 right valid move check and move it
    if (move_1_right is not None) and (board[move_1_right] == '.') :
        new_board = list(board)
        new_board[move_1_right] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})

    #1 left valid move check and move it
    if (move_1_left is not None) and (board[move_1_left] == '.') :
        new_board = list(board)
        new_board[move_1_left] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})
    
    #1 forward valid move check and move it
    if (move_1_forward is not None) and (board[move_1_forward] == '.'):
        new_board = list(board)
        if (is_last_row_check(move_1_forward, board_size, player)):
            new_board[move_1_forward] = player_pieces[-1]
        else:
            new_board[move_1_forward] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})

    #2 right valid move check and move it
    if (move_2_right is not None) and (board[move_2_right] == '.') and (board[move_1_right] == '.'):
        new_board = list(board)
        new_board[move_2_right] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})

    #2 left valid move check and move it
    if (move_2_left is not None) and (board[move_2_left] == '.') and (board[move_1_left] == '.'):
        new_board = list(board)
        new_board[move_2_left] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})

    #2 forward valid move check and move it
    if (move_2_forward is not None) and (board[move_2_forward] == '.') and (board[move_1_forward] == '.'):
        new_board = list(board)
        if (is_last_row_check(move_2_forward, board_size, player)):
            new_board[move_2_forward] = player_pieces[-1]
        else:
            new_board[move_2_forward] = board[current_piece_index]
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 0})

    #2 right jump valid move check and move it
    if (move_2_right is not None) and (board[current_piece_index] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_right])) and (board[move_1_right] not in '$@'):
        new_board = list(board)
        new_board[move_2_right] = board[current_piece_index]
        new_board[move_1_right] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #2 left jump valid move check and move it
    if (move_2_left is not None) and (board[current_piece_index] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_left])) and (board[move_1_left] not in '$@'):
        new_board = list(board)
        new_board[move_2_left] = board[current_piece_index]
        new_board[move_1_left] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #2 forward jump valid move check and move it
    if (move_2_forward is not None) and (board[current_piece_index] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_forward])) and (board[move_1_forward] not in '$@'):
        new_board = list(board)
        if (is_last_row_check(move_2_forward,board_size, player)):
            new_board[move_2_forward] = player_pieces[-1]
        else:
            new_board[move_2_forward] = board[current_piece_index]
        new_board[move_1_left] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #3 right jump valid move check and move it
    if (move_3_right is not None) and (board[move_3_right] == '.') and (board[move_1_right] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_2_right])) and (board[move_2_right] not in '$@'):
        new_board = list(board)
        new_board[move_3_right] = board[current_piece_index]
        new_board[move_2_right] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})
    elif (move_3_right is not None) and (board[move_3_right] == '.') and (board[move_2_right] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_right])) and (board[move_1_right] not in '$@'):
        new_board = list(board)
        new_board[move_3_right] = board[current_piece_index]
        new_board[move_1_right] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})


    #3 left jump valid move check and move it
    if (move_3_left is not None) and (board[move_3_left] == '.') and (board[move_1_left] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_2_left])) and (board[move_2_left] not in '$@'):
        new_board = list(board)
        new_board[move_3_left] = board[current_piece_index]
        new_board[move_2_left] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})
    elif (move_3_left is not None) and (board[move_3_left] == '.') and (board[move_2_left] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_left])) and (board[move_1_left] not in '$@'):
        new_board = list(board)
        new_board[move_3_left] = board[current_piece_index]
        new_board[move_1_left] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})

    #3 forward jump valid move check and move it
    if (move_3_forward is not None) and (board[move_3_forward] == '.') and (board[move_1_forward] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_2_forward])) and (board[move_2_forward] not in '$@'):
        new_board = list(board)
        if (is_last_row_check(move_3_forward, board_size, player)) :
            new_board[move_3_forward] = player_pieces[-1]
        else:
            new_board[move_3_forward] = board[current_piece_index]
        new_board[move_2_forward] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})
    elif (move_3_forward is not None) and (board[move_3_forward] == '.') and (board[move_2_forward] == '.') and (is_opposite_color_piece_present(board[current_piece_index], board[move_1_forward])) and (board[move_1_forward] not in '$@'):
        new_board = list(board)
        if (is_last_row_check(move_3_forward, board_size, player)):
            new_board[move_3_forward] = player_pieces[-1]
        else:
            new_board[move_3_forward] = board[current_piece_index]
        new_board[move_1_forward] = '.'
        new_board[current_piece_index] = '.'
        piece_possible_moves.append({"new_board": ''.join(new_board), "gain": 1})


    return piece_possible_moves

def raichu_moves(board, board_size, player, current_piece_index, player_pieces):
    current_row, current_column = convert_index_to_row_and_column(current_piece_index, board_size)
    #print("current piece: ", board[current_piece_index])
    piece_possible_moves = []
    if player == 'w':
        opposite_players = 'bB$'
    else:
        opposite_players = 'wW@'

    #Forward moves
    for row in range (current_row+1, board_size):
        existing_values = ""
        for forward_row in range(current_row+1, row):
            existing_values = existing_values + board[convert_row_and_column_to_index(forward_row, current_column, board_size)]
        new_existing_values = existing_values.replace(".","")
        if len(new_existing_values) == 0:
            present_index = convert_row_and_column_to_index(row, current_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})
        elif (len(new_existing_values) == 1) and (new_existing_values in opposite_players):
            present_index = convert_row_and_column_to_index(row, current_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                for forward_row in range(current_row+1, row):
                    #if (board[convert_row_and_column_to_index(forward_row, current_column, board_size)] != '.'):
                    new_board[convert_row_and_column_to_index(forward_row, current_column, board_size)] = '.'
                        #break
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})


    #backward moves
    for row in range (current_row-1, -1, -1):
        #print("entered backward move first")
        existing_values = ""
        for back_row in range (current_row-1, row, -1):
            existing_values = existing_values + board[convert_row_and_column_to_index(back_row, current_column, board_size)]
        new_existing_values = existing_values.replace(".", "")
        #print("existing present are not: ", new_existing_values in opposite_players)
        if (len(new_existing_values) == 0):
            present_index = convert_row_and_column_to_index(row, current_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})
        elif (len(new_existing_values) == 1) and (new_existing_values in opposite_players):
            #print("entered front for b")
            present_index = convert_row_and_column_to_index(row, current_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                for back_row in range(current_row-1, row, -1):
                    #if (board[convert_row_and_column_to_index(back_row, current_column, board_size)] != '.'):
                    new_board[convert_row_and_column_to_index(back_row, current_column, board_size)] = '.'
                        #break
                #if(present_index == 27):
                 #    print("new board after left move is : ",''.join(new_board) )
                #print("new board after left move is : ",''.join(new_board) )
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})


    #left moves
    for back_column in range (current_column-1, -1, -1):
        #print("enter left moves")
        existing_values = ""
        for each_col in range (current_column-1, back_column, -1):
            existing_values = existing_values + board[convert_row_and_column_to_index(current_row, each_col, board_size)]
        new_existing_values = existing_values.replace(".", "")
        if (len(new_existing_values) == 0):
            present_index = convert_row_and_column_to_index(current_row, back_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})
        elif (len(new_existing_values) == 1) and (new_existing_values in opposite_players):
            #print("entered left move valid")
            present_index = convert_row_and_column_to_index(current_row, back_column, board_size)
            #print("present index is: ", present_index)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                for each_col in range (back_column, current_column):
                    #if (board[convert_row_and_column_to_index(current_row, each_col, board_size)] != '.'):
                    new_board[convert_row_and_column_to_index(current_row, each_col, board_size)] = '.'
                        #break
                #print("new board after left move is : ",''.join(new_board) )
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})
   

    #right moves
    for forward_column in range (current_column+1, board_size):
        existing_values = ""
        for each_column in range (current_column+1, forward_column):
            existing_values = existing_values + board[convert_row_and_column_to_index(current_row, each_column, board_size)]
        new_existing_values = existing_values.replace(".","")
        if (len(new_existing_values) == 0):
            present_index = convert_row_and_column_to_index(current_row, forward_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})
        elif (len(new_existing_values) == 1) and (new_existing_values in opposite_players):
            present_index = convert_row_and_column_to_index(current_row, forward_column, board_size)
            if (present_index is not None) and (board[present_index] == '.'):
                new_board = list(board)
                new_board[present_index] = board[current_piece_index]
                new_board[current_piece_index] = '.'
                for left_col in range (current_column+1, forward_column):
                    #if (board[convert_row_and_column_to_index(current_row, left_col, board_size)] != '.'):
                    new_board[convert_row_and_column_to_index(current_row, left_col, board_size)] = '.'
                        #break
                piece_possible_moves.append({"new_board": ''.join(new_board), "gain": cost_function(new_board, player)})

        #print("raichu right moves are: ", piece_possible_moves)

    
    
    #North east diagonal moves
    for d in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
        for target_row, target_column in zip(range(current_row + d[0], board_size if d[0] == 1 else -1, d[0]), \
                                      range(current_column + d[1], board_size if d[1] == 1 else -1, d[1])):
            #print(board_size)
            
            diagonal_move = convert_row_and_column_to_index(target_row, target_column, board_size)

            from_col_to_diag = ""
            for diag_row, diag_col in zip(range(current_row + d[0], target_row, d[0]), \
                                        range(current_column + d[1], target_column, d[1])):
                from_col_to_diag += board[convert_row_and_column_to_index(diag_row, diag_col, board_size)]

            from_col_to_diag_without_blank = from_col_to_diag.replace(".", "")
            if len(from_col_to_diag_without_blank) == 0:
                if diagonal_move != None and board[diagonal_move] == ".":
                    new_board = list(board)
                    new_board[diagonal_move] = board[current_piece_index]
                    new_board[current_piece_index] = "."
                    piece_possible_moves.append({ "new_board": ''.join(new_board), "gain": cost_function(new_board, player) })
            elif len(from_col_to_diag_without_blank) == 1 and from_col_to_diag_without_blank in opposite_players:
                if diagonal_move != None and board[diagonal_move] == ".":
                    new_board = list(board)
                    for diag_row, diag_col in zip(range(current_row, target_row, d[0]), \
                                                range(current_column, target_column, d[1])):
                        new_board[convert_row_and_column_to_index(diag_row, diag_col, board_size)] = "."
                    new_board[diagonal_move] = player_pieces[-1] if diagonal_move == (board_size - 1) else board[current_piece_index]
                    new_board[current_piece_index] = "."
                    piece_possible_moves.append({ "new_board": ''.join(new_board), "gain": cost_function(new_board, player) })


    return piece_possible_moves
        

def randomize(l: list):
    board_size = len(l)
    for i in range(0, board_size):
        rand_index = random.randint(0, board_size - 1)
        l[rand_index], l[i] = l[i], l[rand_index]

def successors(board: str, board_size: int, player: str):
    pieces = get_player_pieces(player)
    pieces_index = [i for i in range(len(board)) if board[i] in pieces]
    #print(pieces, pieces_index)

    Total_moves = []
    for piece_pos in pieces_index:
        piece = board[piece_pos]
        if piece in "bw":
            Total_PieceMoves = pichu_moves(board, board_size, player, piece_pos, pieces)
            #print("all piecemoves are : ", Total_PieceMoves)
            #print("Pichu moves are : ", Total_PieceMoves)
            Total_moves += Total_PieceMoves
            #break
        elif piece in 'BW':
            Total_PieceMoves = pikachu_moves(board, board_size, player, piece_pos, pieces)
            #print("all pikachu piecemoves are : ", Total_PieceMoves)
            #print("Pikachu moves are : ", Total_PieceMoves)
            Total_moves += Total_PieceMoves
            #break
        elif piece in "$@":
            moves = raichu_moves(board, board_size, player, piece_pos, pieces)
            #print("raichu moves are: ", moves)
            Total_moves += moves
    

    #print("moves are: ", Total_moves)

    randomize(Total_moves)

    Total_moves.sort(key=lambda x: x["gain"])

    result = []
    for move in Total_moves:
        if move["new_board"] not in result:
            result.append(move["new_board"])
    #print("all sucessors are: ", result)
    return result

def get_opponent_pieces(player: str):
    return "bB$" if player.lower() != "b" else "wW@"

def cost_function(board: str, player: str, thresh_value: int = 0.5, max_thresh_value: int = 1.0):
    #print("entered calculate cost")
    pieces = get_player_pieces(player)
    pieces_count = sum([board.count(piece) for piece in pieces])
    player_points = board.count(pieces[0]) + board.count(pieces[1]) *350  + board.count(pieces[2]) * 3000
    opp_pieces = get_opponent_pieces(player)
    opp_pieces_count = sum([board.count(piece) for piece in opp_pieces])
    opponent_points = board.count(opp_pieces[0])+ board.count(opp_pieces[1]) * 350 + board.count(opp_pieces[2]) * 3000

    threshold = thresh_value / max_thresh_value

    return ((pieces_count + (player_points * threshold)) - (opp_pieces_count)+(opponent_points * (1 - threshold)))

#took the reference for minimax algorithm from below link
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
def max_move(board, board_size, alpha, beta, player, total_height, current_height, timelimit):

    current_player_successors = successors(board, board_size, player)
    

    if (player.lower() == 'b'):
        current_player_successors.reverse()
    if (current_height == total_height) or (len(current_player_successors) == 0):
        return  (board, cost_function(board, player))
    
    current_max_value = -math.inf
    current_max_board = None
    current_alpha = alpha
    for suc in current_player_successors:
        response_from_min = min_move(suc, board_size, current_alpha, beta, player, total_height, current_height+1, timelimit)

        if (current_max_value < response_from_min[1]):
            current_max_value = response_from_min[1]
            current_max_board = suc
        
        current_alpha = max(current_alpha, current_max_value)

        if (current_alpha >= beta):
            break
    
    
    
    return (current_max_board, current_max_value)



def min_move(board, board_size, alpha, beta, player, total_height, current_height, timelimit):
    current_player_successors = successors(board, board_size, player)

    if (player.lower() == 'b'):
        current_player_successors.reverse()
    if (current_height == total_height) or (len(current_player_successors) == 0):
        return  (board, cost_function(board, player))

    current_min_value = math.inf
    current_min_board = None
    current_beta = beta 

    for successor in current_player_successors:
        response_from_max = max_move(successor, board_size, alpha, current_beta, player, total_height, current_height+1, timelimit)

        if (current_min_value > response_from_max[1]):
            current_min_value = response_from_max[1]
            current_min_board = successor
        
        current_beta = min(current_beta, current_min_value)

        if (alpha >= current_beta):
            break

    #print ("max succa re: ", current_min_board, current_min_value)
    return (current_min_board, current_min_value)


def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    #while True:
     #   time.sleep(1)
      #  yield board
      #successors(board, N, player)

      # Signal handler code based on the method described in the below link:
    #   - https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
    def signal_handler(sig, frame):
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    current_height = 1

    while True:
        result = max_move(board, N, -math.inf, math.inf, player, current_height, 0, timelimit)
        yield result[0]
        current_height += 1


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    #find_best_move(board, N, player, timelimit)
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
