
class Neuron:
  def __init__(self, inbound_neurons = []):
    # properties will go here
    
    # Neuron from which this neuron receives values
    self.inbound_neurons = inbound_neurons
    
    # Neuron to which this neuron passes values
    self.outbound_neurons = []
    
    # For each inbound neuron here, add this neuron as an outbound neuron there
    for n in self.inbound_neurons:
      n.outbound_neurons.append(self)
      
    # Initialize a calculated value
    self.value = None
