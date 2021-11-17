
# a list of functions that are used throughout 

def means_squared_error(actual,prediction):
    return ((actual-prediction)**2).mean(axis=0)

tar_x, tar_y = 0,0
def target(coordinates):
    global tar_x, tar_y
    return means_squared_error(coordinates,[tar_x,tar_y])

def assess_fitness(particle,target):
    return target(particle)
