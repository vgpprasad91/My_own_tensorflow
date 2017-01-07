
def topological_sort(input_nodes_dict):
  """
  Sort generic nodes in topological sort using Khan's algorithm
  'input_nodes_dict': A dictionary where the key is a 'Input' node and the value is the respective value feed to that node
  Returns a list of sorted node
  """
  
  input_nodes = [n for n in input_nodes_dict]
  
  
