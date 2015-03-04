# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    policy_row = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    #policy = [list(policy_row) for row in xrange(len(forward))]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
            [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
            [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
            [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    value_row = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    #value = [list(value_row) for row in xrange(len(forward))]   
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    def is_valid_point(next_point, grid):
        len_x_grid = len(grid) 
        len_y_grid = len(grid[0])        
        if next_point[0] >= 0 and next_point[1] >=0 :
            if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                if grid[next_point[0]][next_point[1]]!=1:
                    return True
        return False  
    
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    change = True
    
    
    while change:
        change = False
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                for orientation in xrange(len(forward)):
                    if [x,y] == goal:
                        if value[orientation][x][y] >0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True
                    elif is_valid_point((x,y), grid):
                            for i in xrange(len(action)):
                                o2 = (orientation +action[i]) %4
                                x2 = x + forward[o2][0]
                                y2 = y + forward[o2][1]
                                if is_valid_point((x2,y2), grid):
                                    v2 = value[o2][x2][y2] +cost[i]
                                    if v2 < value[orientation][x][y]:
                                        value[orientation][x][y] = v2
                                        policy[orientation][x][y] = action_name[i]
                                        change = True

    print policy, "\n"
    
    print value, "\n" 
    
    x,y,orientation =  init
    policy2D[x][y] = policy[orientation][x][y]

    while policy2D[x][y] !='*':
        if policy2D[x][y] == '#':
            o2 = orientation
        elif policy2D[x][y] == 'R': 
            o2 = (orientation -1) %4
        elif policy2D[x][y] == 'L':
            o2 = (orientation +1) %4   
        x = x + forward[o2][0]
        y = y +forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]

        #print  "new", policy2D[x][y], x,y
    
    return policy2D

pol2D = optimum_policy2D(grid,init,goal,cost)

for row in pol2D:
    print row