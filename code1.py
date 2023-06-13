class TicTacToeGame:
    '''This class is regarding Tic Tac Toe Board Game'''
    def __init__(self):
        self.grid = [[" " for i in range(3)] for j in range(3)]
        
    def utility(self, player, count):
        if player == "X": # "x" won
            return 1
        elif player == "O": # "x" lost
            return -1
        elif count == 6: # draw match
            return 0
        
    def IsTerminal(self, state):
        count = 0
        # checking all rows
        for i in range(3):
            if state[i][0] != " " and state[i][1] != " " and state[i][2] != " ":
                count += 1
                if state[i][0] == state[i][1] and state[i][0] == state[i][2]:
                    return True, self.utility(state[i][0], count)
        
        # checking all columns
        for j in range(3):
            if state[0][j] != " " and state[1][j] != " " and state[2][j] != " ":
                count += 1
                if state[0][j] == state[1][j] and state[0][j] == state[2][j]:
                    return True, self.utility(state[0][j], count)

        # checking diagonals
        if state[0][0] != " " and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
            return True, self.utility(state[0][0], count)
        if state[0][2] != " " and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
            return True, self.utility(state[0][2], count)
        
        if count == 6:
            return True, self.utility(None, count)
        return False, None
    
    def next_states(self, state, player):
        states = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    temp = []
                    for row in state:
                        temp.append(row.copy())
                    temp[i][j] = player
                    states.append(temp)
        return states
    
    def min_max_search(self, depth, leaves):
        isterminal, assumed_utility = self.IsTerminal(self.grid)
        if isterminal is True:
            leaves[0] += 1
            depth[0] = 1
            return
        
        value, state, final_depth = self.max_value(self.grid, 1, leaves)
        depth[0] = final_depth
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = state[i][j]
        return 
    
    def max_value(self, state, depth, leaves):
        isterminal, assumed_utility = self.IsTerminal(state)
        if isterminal is True:
            leaves[0] += 1
            return assumed_utility, state, 1
        
        assumed_max = float("-inf")
        assumed_state = None
        states = self.next_states(state, "X")
        
        final_depth = float("-inf")
        assumed_depth = float("inf")
        for s in states:
            temp_max, temp_state, temp_depth = self.min_value(s, depth, leaves)
            final_depth = max(final_depth, temp_depth)
            if temp_max > assumed_max:
                assumed_max = temp_max
                assumed_state = s
                assumed_depth = temp_depth
            elif temp_max == assumed_max and assumed_depth > temp_depth: # chossing stateswith minimum depth
                assumed_state = s
                assumed_depth = temp_depth
        return assumed_max, assumed_state, depth + final_depth
    

    def min_value(self, state, depth, leaves):
        isterminal, assumed_utility = self.IsTerminal(state)
        if isterminal is True:
            leaves[0] += 1
            return assumed_utility, state, 1
        
        assumed_min = float("inf")
        assumed_state = None
        states = self.next_states(state, "O")
        
        assumed_depth = float("inf")
        final_depth = float("-inf")
        for s in states:
            temp_min, temp_state, temp_depth = self.max_value(s, depth, leaves)
            final_depth = max(final_depth, temp_depth)
            if temp_min < assumed_min:
                assumed_min = temp_min
                assumed_state = s
                assumed_depth = temp_depth
            elif temp_min == assumed_min and assumed_depth > temp_depth:
                assumed_state = s
                assumed_depth = temp_depth
        return assumed_min, assumed_state, depth + final_depth
