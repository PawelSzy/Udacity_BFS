# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    len_x_grid = len(grid) 
    len_y_grid = len(grid[0])

    visited = []
    frontier = [[0,goal]]
    value[goal[0]][goal[1]] = 0
    
    policy[goal[0]][goal[1]] = '*'
    
    def point_into_policy(point, next_point):
        
        x2,y2 = next_point
        x1,y1 = point
        if x2 - x1 == 1:
            policy = 'v'
        if x2 - x1 == -1:
            policy = '^'
        if y2 - y1 == 1:
            policy = '>'
        if y2 - y1 == -1:
            policy = '<'     
        return policy
    
    def is_valid_point(next_point):
        if next_point[0] >= 0 and next_point[1] >=0 :
            if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                if grid[next_point[0]][next_point[1]]!=1:
                    return True
        return False  
    
    
    def min_value_of_neighbors(point, grid, value):
        #return a value of neighbors with min value of values table (min moves to goal)
        min_value = 99
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point,kierunek) ]
            if is_valid_point(next_point):
                next_x, next_y = next_point[0], next_point[1]
                if min_value > value[next_x][next_y]:
                    min_value = value[next_x][next_y]
                    point_of_min_value = (next_x, next_y)
        return min_value, point_of_min_value       
    
    
    
    while len(frontier)!=0:
        point = frontier.pop()
        visited.append(point[1])
        x = point[1][0]
        y = point[1][1]
        point_value =  value[x][y]
        if point[1] != goal:
            min_value, point_of_min_value = min_value_of_neighbors(point[1], grid, value)
            value[x][y]  = min_value + 1
            policy[x][y] = point_into_policy(point[1], point_of_min_value)
        
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point[1],kierunek) ]   
            if is_valid_point(next_point) and next_point not in visited :
                point_cost = point[0]
                new_cost = point_cost +cost
                new_point = [new_cost, next_point]
                             
                frontier.append(new_point)
                
                
        
    #return value 

    return policy


new_grid = optimum_policy(grid,goal,cost)
for row in new_grid:
    print row