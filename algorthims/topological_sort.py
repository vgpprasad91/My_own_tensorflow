
def topological_sort(input_nodes_dict):
  """
  Sort generic nodes in topological sort using Khan's algorithm
  'input_nodes_dict': A dictionary where the key is a 'Input' node and the value is the respective value feed to that node
  Returns a list of sorted node
  """
  
  input_nodes = [n for n in input_nodes_dict.keys()]
  
  graph = {}
  nodes= [n for n in input_nodes]
  while len(nodes) > 0:
    n = nodes.pop(0)
    if n not in graph:
      graph[n] = {'in': set(), 'out': set()}
    for m in n.outbound_nodes:
      if m not in graph:
        graph[m] = {'in':set(), 'out':set()}
      graph[n]['out'].add(m)
      graph[m]['in'].add(n)
      nodes.append(m)
  L = []
  S = set(input_nodes)
  while len(S) > 0:
    n = S.pop(0)
    if isinstance(
  
  
