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

delta = forward

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
    #value = [[float('inf') for row in range(len(grid[0]))] for col in range(len(grid))]    
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    cost_matrix = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    len_x_grid = len(grid) 
    len_y_grid = len(grid[0])
    
    cost_temp = 1
    
    def is_valid_point(next_point):
        if next_point[0] >= 0 and next_point[1] >=0 :
            if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                if grid[next_point[0]][next_point[1]]!=1:
                    return True
        return False 
    
    
    def direction_into_vector(direction):
        #use globals forward, forward_name
        return forward(direction)
    
    def cost_between_points(point, next_point, cost):
        # point [row,col,direction]
        #next_point [row,col]
        #cost [right turn, no turn, left turn]
        #return (cost, action, action_name)
        #print point
        #warunek prostopadlosci wektorw
        #ax*bx+ay*by=0
        ax,bx = forward[point[2]]
        ay = point[0]-next_point[0]
        by = point[1]-next_point[1]
        
        #print ax,bx, ay, by
        if ax*bx + ay +by !=0:
            #vektory nie sa prostopadle
            #ruch do przody
            i = 1

        elif ax*by == - 1 or bx*ay == -1:
            #ruch w prawo:
            i = 0
        else:
            #ruch w lewo
            i = 2
        
        #print "return", i, cost[i], action[i], action_name[i]
        return (cost[i], action[i], action_name[i])    
    
    def min_value_of_neighbors(point, grid, value):
        #return a value of neighbors with min value of values table (min moves to goal)
        if point == goal:
            return 0
        min_value =  99 #float('inf')
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point,kierunek) ]
            if is_valid_point(next_point):
                #print 'valid'
                next_x, next_y = next_point[0], next_point[1]
                #print "x,y,value: ", next_x, next_y,  value[next_x][next_y]
                if min_value > float(value[next_x][next_y]):
                    min_value = value[next_x][next_y]
                    #print "min_value", min_value
        return min_value  
    
    #frontier = [[0,goal]] 
    frontier = []
    #right
    for kierunek in xrange(len(forward)):
        x_dum, y_dum =  forward[kierunek]
        new_point = [goal[0] + x_dum, goal[1] + y_dum, kierunek]
        if is_valid_point(new_point):
            frontier.append([0,new_point])
            cost_matrix[new_point[0]][new_point[1]] = cost_between_points(new_point, [goal[0], goal[1]], cost)[0]
            #print cost_between_points(new_point, [goal[0], goal[1]], cost)
    
    
    value[goal[0]][goal[1]] = 0
    visited = []
    while len(frontier)!=0:
        point = frontier.pop()
        visited.append(point[1])
        x = point[1][0]
        y = point[1][1]
        direction = point[1][2]
        
        #print "point", point
        if point[1] != goal: 
            value[x][y] = min_value_of_neighbors(point[1], grid, value) + 1
            
        else:
           value[x][y] =0 
           cost_matrix[x][y] = '*'
        #if point[1] != goal:
            #min_value, point_of_min_value = min_value_of_neighbors(point[1], grid, value)
            #value[x][y]  = min_value + 1
            #policy[x][y] = point_into_policy(point[1], point_of_min_value)

        
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point[1],kierunek) ]   
            if is_valid_point(next_point) and next_point not in visited :
                point_cost = point[0]
                new_cost = point_cost +cost_temp

                
                #add min cost of move !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print "[point]", point
                move_cost, change_direction, move_symbol = cost_between_points(point[1], next_point, cost)
                #print "ret", ret
                new_direction = direction + change_direction
                print "next_point", next_point
                next_point = [next_point[0], next_point[1], new_direction] 
                print "next_point", next_point
                new_point = [new_cost, next_point]
                print "new_point", new_point
                
                frontier.append(new_point)    
    
    
    return value, cost_matrix
    return policy2D

policy, cost_matrix = optimum_policy2D(grid,init,goal,cost)
for row in policy:
    print row
    
for row in cost_matrix:
    print row