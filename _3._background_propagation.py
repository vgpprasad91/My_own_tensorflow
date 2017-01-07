
# Create a class Neuron
class Neuron:
  
  # instantiate all the values for the neuron class
  def __init__(self,inbound_neurons=[]):
    
    # Assign the values for the inbound_neurons
    self.inbound_neurons = inbound_neurons
    
    # Assign the values for the outbound_neurons
    self.outbound_neurons = []
    
    # Assign the values for the output calculated values
    self.value = None
    
    # Add this node as an outbound node on its inputs
    for n in self.inbound_neurons:
      n.outbound_neurons.append(self)
    
  def backward(self):
    raise NotImplemented
