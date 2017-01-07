
# Create a class Input Neuron
class Input(Neuron):
  
  # Initialize all the values
  def __init__(self):
    
    # An input neuron has no inbound_neurons
    Neuron.__init__(self)
    
    # Create a function for forward propagation from input neurons
    def forward_propagation(self,value=None):
      # Overwrite the calculated value if one is passed in
      if value is Not None:
        self.value = value
