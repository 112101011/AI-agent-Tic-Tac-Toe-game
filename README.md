# Tic-Tac-Toe-game
This is a competetive envionment where one player tries to maximises its performence which in turn will minimise the performance of other
player.

This kids of environments lead to adversial search, where two (or) agents have conflicting goals.

This is a zero-sum game(what is good for one player is not good for other, that is there is no win-win (or) lose-lose situation).

If we consider each cell in the board to distinct, the number of valid states in this game would be less than 3^(9) [upper bound]. Because it 
is the number of functions from 9 cells to {X, O, blank}.

Here it is very important to note that player 'X' (that is AI agent) is not taking any risks since it assumes that the opponent always play 
optimally. Code is also written accordingly. If 'X' assumes that opponent 'O' plays sub-optimally it can take risks accordingly.

Here, in the program minimax algorithm is implemented where it assumes that players play optimally. The minmax algorithm performs a complete 
depth-first search exploration of the Game Tree If the maximum depth of the Tree is m and there are b legal moves at each point. 
Time complexity: O(b^(m)) and space complexity is O(bm) [in general]. Later the performance can be improved by aplha-beta pruining. 

code1.py contains TicTacToe class written using minimax search without alpha-bheta pruning.
code2.py contains TicTacToe1 class written using minimax search with aplha-bheta pruning.
The comparision gives a good idea about the advantage of pruning in game search.
