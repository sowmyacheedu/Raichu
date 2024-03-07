# **Raichu**
* The given problem is a raichu game where the goal is to give the next optimal move for the given player and the given board state

## ***Problem Formulation***
* The initial State is the value provided in the 3rd argument(board state) while running the program

* The Successor function returns the list of all possible moves that can be moved from the given position(depending on the current piece:- Pichu, Pikachu or Raichu)
* each separate function is written for each moves(pichu_moves(), pikachu_moves(), raichu_moves())
* we are using randomization after getting all the successors, because successors genearated by the code will always have a similar order due to the way the moves are being generated or written in pichu, pikachiu, raichu and using gain value we are sorting them before proceding with aplha beta pruning algorithm.

* The cost function takes input parameters-> board,  player, thresh_value, max_thresh_value it returns the cost value at each possible state using thresh_value (we are using total pieces count + (diff of pieces count of current players).

* The search pattern used to find the best move is alpha-beta pruning(in minimax algorithm). In general minimax algorithm works by assuming the opponent as the best player(who makes optimal moves) thus it checks all the possible moves, alpha-beta pruning helps in reducing the time by cutting off the moves which don’t have a chance of giving optimal move thus optimizing the code.

* construction of evluation function e(s) = (player pieces - opposite pieces)


## ***Problems Faced:***
* Faced difficulty in writing the code for raichu moves especially diagonal moves since they have many possibilities without any particular pattern in rows, column number.

* For the Search algorithm initially we used minimax, but faced difficulty to get the optimal move in less time hence solved this issue by implementing alpha-beta pruning in the minimax.
