# Tuple => is similar to a list but is immutable, meaning its contents cannot be changed once defined.

# e.g - if I wanted to have a list of 3-d coordinates, the natural python representation would be a list of tuples,
# where each tuple is size 3 holding one (x, y, z) group. 

tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])    ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
