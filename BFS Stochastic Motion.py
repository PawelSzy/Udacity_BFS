# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    def is_valid_point(next_point, grid):
        len_x_grid = len(grid) 
        len_y_grid = len(grid[0])        
        if next_point[0] >= 0 and next_point[1] >=0 :
            if next_point[0] < len_x_grid and next_point[1] < len_y_grid:
                if grid[next_point[0]][next_point[1]]!=1:
                    return True
        return False      
    
    def value_of_point((x,y),value, grid, collision_cost):
        len_x_grid = len(value) 
        len_y_grid = len(value[0])
        if (x < 0) or (y <0) or (x >= len_x_grid)  or (y >=len_y_grid) or grid[x][y]==1 :
            return collision_cost
        else:
            return value[x][y]

    def new_x2_y2(x,y,orientation):
        x2 = x + delta[orientation][0]
        y2 = y + delta[orientation][1]
        return x2,y2
    
    def orient_to_min_valu(x,y,value,grid, delta, collision_cost):
        #return orientation to point with min_value
        min_value = 1000
        return_orient = False
        for orientation in xrange(len(delta)):
            x2,y2 = new_x2_y2(x,y, orientation) 
            point_value = value_of_point((x2,y2),value, grid,collision_cost) 
            #print [orientation], [x2,y2], point_value
            if point_value < min_value:
                #print "next", point_value, min_value
                min_value = point_value
                return_orient = orientation
        return return_orient 
    
    #value[goal[0]][goal[1]] = 0
    change = True
    

    i = 0
    while change:
        change = False  
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                for orientation in xrange(len(delta)):
                    if [x,y] == goal:
                        if value[x][y] > 0:
                            value[x][y] = 0
                            policy[x][y] = '*'
                            change = True
                    elif is_valid_point((x,y), grid):
                        #orientation = orient_to_min_valu(x,y,value,grid, delta, collision_cost)

                        # go left
                        o_left = (orientation + 1) %4 
                        x2,y2 = new_x2_y2(x,y,o_left)
                        v_left  =  value_of_point((x2,y2),value, grid, collision_cost) 
                        #go right
                        o_right = (orientation - 1) %4 
                        x2,y2 = new_x2_y2(x,y,o_right)
                        v_right = value_of_point((x2,y2),value, grid, collision_cost)                             
                        x2,y2 = new_x2_y2(x,y,orientation)
                        #go straith-idz prosto
                        v_straigh =  value_of_point((x2,y2),value,grid, collision_cost)                        
                        
                        
                        v2 = v_straigh*success_prob + v_right*failure_prob + v_left*failure_prob +cost_step

                        #value[x][y] = v2
                        #policy[x][y] = delta_name[orientation]
                        #change = True
                        if v2 <value[x][y]:
                            value[x][y] = v2
                            policy[x][y] = delta_name[orientation]
                            change = True
                        #else:
                            #change = False
        #i += 1
        #if i >30:
            #change = False               
    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
        
#grid = [[0,0,0],[0,0,0]]        
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5



value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print row
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 1000.00, 1000.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
