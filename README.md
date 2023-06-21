# Tic-Tac-Toe-game

## Problem statement
Design an AI agent to play the tic-tac-toe game against the user. 

The Tic-Tac-Toe game starts on a 3x3 grid with two players "X" and "O" who take turns and play. 
The rules are as follows: 
  1) Each player gets a turn with player "X" (resp. "O") writing an "X" (resp. "O") in an empty cell of the grid. 
  2) The game starts with the move of the "O" player. 
  3) The first player to write on three horizontal or vertical or diagonal cells wins.
  4) The player who wins gets 1 point, the player who loses gets -1 point. If a match draws then each player gets 0 points.
  5) The locations in the grid are as follows:<br/>
     ![image](https://github.com/112101011/Tic-Tac-Toe-game/assets/111628378/9ab470a3-2758-477c-8006-2f8984612307) <br/>
Here the AI agent places 'X' optimally. Where as the user(we) places 'O' optimal (or) sub-optimal depends on the user.

Example for the player 'X' winning: <br/>
![image](https://github.com/112101011/Tic-Tac-Toe-game/assets/111628378/3d72b9ad-5b0e-4575-9529-6b53dd4b2ee7)

Example for the player 'O' winning: <br/>
![image](https://github.com/112101011/Tic-Tac-Toe-game/assets/111628378/678b7322-2a06-475b-8188-f69c99d98020)


## Approach

1) This is a competetive envionment where one player tries to maximises its performence which in turn will minimise the performance of other player.
2) This kind of environments lead to adversial search, where two (or) more agents have conflicting goals.
3) This is a zero-sum game(what is good for one player is not good for other, that is there is no win-win (or) lose-lose situation).
4) If we consider each cell in the board to distinct, the number of valid states in this game would be less than 3^(9) [upper bound]. Because it is the number of functions from 9 cells to {X, O, blank}.
5) Here it is very important to note that player 'X' (that is AI agent) is not taking any risks since it assumes that the opponent always play optimally. Code is also written accordingly. If 'X' assumes that opponent 'O' plays sub-optimally it can take risks accordingly.

Here, in the program minimax algorithm is implemented where it assumes that players play optimally. The minimax algorithm performs a complete 
depth-first search exploration of the Game Tree If the maximum depth of the Tree is m and there are b legal moves at each point. 
Time complexity: O(b^(m)) and space complexity is O(bm) [in general]. Later the performance can be improved by aplha-beta pruining. <br/>

Game Tree: <br/>
![image](https://github.com/112101011/Tic-Tac-Toe-game/assets/111628378/d60eaf4e-0c65-4cb4-bf75-69d5708e3b28) <br/>

File MiniMax search.ipynb contains TicTacToe class written using minimax search without alpha-bheta pruning. <br/>
File Alpha Beta pruning.ipynb contains TicTacToe1 class written using minimax search with aplha-bheta pruning. <br/>
The comparision between MiniMax search and MiniMax search using alpha beta pruning gives a good idea about the advantage of pruning in game theory. We can observe the advantage of alpha-beta pruning by noticing that the number of leaves in a Game tree without pruning is around 25,000 whereas after pruning it became around 1000.<br/>
One example of alpha beta pruning:<br/>
![image](https://github.com/112101011/Tic-Tac-Toe-game/assets/111628378/b5ebb189-ef22-4217-8fe5-34ccff698ab5)

