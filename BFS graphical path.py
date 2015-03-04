# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    def path_into_graph(path,grid):
        
        row = [' ' for x_dummy in range(len(grid[0]))]
        new_path = [list(row) for x_dummy in range(len(grid))]
        
        for i in xrange((len(path)-1)):
            x2,y2 = path[i+1][1]
            x1,y1 = path[i][1]
            if x2 - x1 == 1:
                new_path[x1][y1] = 'v'
            if x2 - x1 == -1:
                new_path[x1][y1] = '^'
            if y2 - y1 == 1:
                new_path[x1][y1] = '>'
            if y2 - y1 == -1:
                new_path[x1][y1] = '<'    

        
        x_last,y_last = path[-1][1]
        #print "x_last,y_last", x_last,y_last
        new_path[x_last][y_last] = "*"
        return new_path
    
    
    visited = []
    frontier = [[[0,init]]]
    path = []
    len_x_grid = len(grid) 
    len_y_grid = len(grid[0])
    while len(frontier)!=0:
        path = frontier.pop(0)
        #print "path", path
        if path[-1][1] == goal:
            #print "znalazle", path[-1]
            return path_into_graph(path,grid)
        for kierunek in delta:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(path[-1][1],kierunek) ]
            #print "next_point", next_point
            if next_point[0] >= 0 and next_point[1] >=0 :
                   if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                       if next_point not in visited and grid[next_point[0]][next_point[1]]!=1:
                           new_cost = path[-1][0] +cost
                           new_path = path + [[new_cost, next_point]]
                           frontier.append(new_path) 
                           visited.append(next_point)
                        
                    
    return 'fail'    

print search(grid,init,goal,cost)
