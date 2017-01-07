
# create a class neuron
class Neuron:
  
  # Instantiate all the necessary values using the __init__ function
  def __init__(self, inbound_neurons = []):
    
    # Instantiate the inbound_neurons
    self.inbound_neurons = inbound_neurons
    
    # Instantiate the outbound_neurons
    self.outbound_neurons = []
    
    # Instantiate the value to be calculated
    self.value = None
    
    # Add this node as an outbound node on its inputs
    for n in self.inbound_neurons:
      n.outbound_neurons.append(self)
      
  # create a function for forward propagation
  
  def forward_propagation(self):
    raise NotImplemented
    
  # create a function for backward propagation
  
  def backward_propagation(self):
    raise NotImplemented
