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
def is_valid_point(next_point, len_x_grid, len_y_grid):
    if next_point[0] >= 0 and next_point[1] >=0 :
        if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
            if grid[next_point[0]][next_point[1]]!=1:
                return True
    return False 


class Point:
    def __init__(self, x,y,direction, point_cost=0, steps_from_goal = 0):
        self.x = x
        self.y = y
        self.direction = direction
        self.cost = point_cost
        self.steps_from_goal = steps_from_goal
        
    def is_valid_point(self, len_x_grid, len_y_grid):
        if self.x >= 0 and self.y >=0 :
            if self.x < len_x_grid and self.y < len_y_grid:
                if grid[self.x][self.y]!=1:
                    return True
        return False
    def __str__(self):
            print "point:"
            print "x,y:", self.x, self.y
            print "direction:", self.direction
            print "steps_from_goal:", self.steps_from_goal

    def return_X_Y(self):
            return [self.x, self.y]
            
    def is_point_X_Y(self, x,y):
        if x.self == x and x.self.y == y:
            return True
        else:
            return False
     
    def direction_index(self):    
        index = forward_name.index(self.direction)
        return index
    
    def direction_vector(self):
        #zwraca wektor kierunku po podaniu pisemnego kierunku np. "up" -> return [-1, 0]
        index = forward_name.index(self.direction)
        return forward[index]
        
    def cost_between_points(self, next_point, cost):
        # point [row,col,direction]
        #next_point [row,col]
        #cost [right turn, no turn, left turn]
        #return (cost, action, action_name)
        #print point
        #warunek prostopadlosci wektorw
        #ax*bx+ay*by=0
        ax,ay = self.direction_vector()
        #print ax, ay
        bx = self.x-next_point[0]
        by = self.y-next_point[1]
        #print bx, by   
        #print ax*bx + ay*by
        
        if ax*bx + ay*by !=0:
            #vektory nie sa prostopadle
            #ruch do przody
            i = 1

        else:
            if ax*by == - 1 or bx*ay == -1:
                #ruch w prawo:
                i = 0
            else:
                #ruch w lewo
                i = 2
        #print "return",  cost[i], action[i], action_name[i], i
        return (cost[i], action[i], action_name[i], i)         
        
        
    def min_value_of_neighbors(self, grid, value):
        #return a value of neighbors with min value of values table (min moves to goal)
        if self.return_X_Y() == goal:
            return 0
        len_x_grid = len(grid) 
        len_y_grid = len(grid[0])
        
        min_value =  99 #float('inf')
        for kierunek in forward:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(self.return_X_Y(),kierunek) ]
            if is_valid_point(next_point, len_x_grid, len_y_grid):
                next_x, next_y = next_point[0], next_point[1]
                if min_value > float(value[next_x][next_y]):
                    min_value = value[next_x][next_y]

        return min_value             
            
def optimum_policy2D(grid,init,goal,cost):
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    cost_matrix = [['|' for row in range(len(grid[0]))] for col in range(len(grid))]
    len_x_grid = len(grid) 
    len_y_grid = len(grid[0])
    
    initial_point = Point(goal[0], goal[1], 'left', 0)
    #initial_point = Point(init[0], init[1], direction =forward_name[init[2]], point_cost = 0)
    frontier = [initial_point]
    #print initial_point
    
    visited = []
    #cost.reverse()
    while len(frontier)!=0:
        point = frontier.pop()
        visited.append([point.x, point.y])
        #print visited
        
        #points from goal
        if point.return_X_Y() == goal:
            print "goal", goal
            value[point.x][point.y] =0 
            cost_matrix[point.x][point.y] = '*'
        else:
            value[point.x][point.y] = point.min_value_of_neighbors(grid, value) + 1
            cost_matrix[point.x][point.y]= point.cost
            
        #BFS - breath first search    
        for kierunek in forward:
            next_point = [x_or_y + strona_swiata for x_or_y, strona_swiata in zip(point.return_X_Y() ,kierunek) ] 
            #print next_point
            if is_valid_point(next_point, len_x_grid, len_y_grid) and next_point not in visited :
                point_steps = point.steps_from_goal
                new_steps = point_steps +1
                #print point.x, point.y
                #print next_point
                
                x,y = next_point
                new_cost, new_action, action_name, move_index = point.cost_between_points(next_point, cost)
                #print new_cost, new_action, action_name
                #new_cost = cost[-new_action]
                #cost_matrix[x][y]= new_cost
                #print "new_cost, new_action, action_name", new_cost, new_action, action_name
                new_direction_index = (point.direction_index() + new_action) % len(forward_name) 
                new_cost += point.cost
                direction_name = forward_name[new_direction_index]
                new_point = Point( x,y,direction = direction_name, point_cost=new_cost, steps_from_goal = new_steps)
                frontier.append(new_point)
                
                
    return value, cost_matrix
    return policy2D



policy, cost_matrix = optimum_policy2D(grid,init,goal,cost)
for row in policy:
    print row
    
for row in cost_matrix:
    print row
    
    
print "\n"
#p = Point(3,4, direction = 'left', point_cost=0, steps_from_goal = 0)
#print p.cost_between_points([4,4], cost)