
# import from myflow
from myflow import *

# Intialize the inputs
x,y,z = Input(), Input(), Input()
inputs = [x,y,z]

# Intialize the weights
wt_x, wt_y, wt_z = Input(), Input(), Input()
weights = [wt_x, wt_y, wt_z]

# Initialize the bias
bias = Input()

# Call the linear function and pass the inputs, weights and bias as parameters
f = Linear(inputs, weights, bias)

# create a dictionary by initializing a random value for the inputs, weights and bias

feed_dict = { x:8, y:10, z:2, wt_x: 0.5, wt_y: 0.1, wt_z : 0.8}

# perform a topological sort of the graph
graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

print(output)
