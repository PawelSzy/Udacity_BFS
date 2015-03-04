# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    row = [99 for x_dummy in range(len(grid[0]))]
    value = [list(row) for x_dummy in range(len(grid))]
    len_x_grid = len(grid) 
    len_y_grid = len(grid[0])
    print goal

    def is_valid_point(next_point, visited):
        if next_point[0] >= 0 and next_point[1] >=0 :
            if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                if grid[next_point[0]][next_point[1]]!=1:
                    return True
        return False  
    
    def min_value_of_neighbors(point, grid, value, visited):
        #return a value of neighbors with min value of values table (min moves to goal)
        min_value = 99
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point,kierunek) ]
            if is_valid_point(next_point, visited):
                next_x, next_y = next_point[0], next_point[1]
                if min_value > value[next_x][next_y]:
                    min_value = value[next_x][next_y]
        return min_value            
                
                           
    visited = []
    frontier = [[0,goal]]
    value[goal[0]][goal[1]] = 0
    #print frontier
    while len(frontier)!=0:
        point = frontier.pop()
        visited.append(point[1])
        x = point[1][0]
        y = point[1][1]
        point_value =  value[x][y]
        if point[1] != goal:
            value[x][y] = min_value_of_neighbors(point[1], grid, value, visited) + 1
        
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point[1],kierunek) ]   
            if is_valid_point(next_point, visited) and next_point not in visited :
                point_cost = point[0]
                new_cost = point_cost +cost
                new_point = [new_cost, next_point]
                             
                frontier.append(new_point)
                
                
        
    return value 

new_grid = compute_value(grid,goal,cost)
for row in new_grid:
    print row