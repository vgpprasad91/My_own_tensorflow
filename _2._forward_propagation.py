class neuron:
  
  #initialite all the values using __init__ function
  def __init__(self,inbound_neurons=[]):
    
    # Add a code to assign inbound_neurons
    self.inbound_neurons = inbound_neurons
    
    # Add a code to assign outbound_neurons
    self.outbound_neurons = []
    
    # Add this node as an outbound node on its inputs
    for n in self.inbound_neurons:
      n.outbound_neurons.append(self)
    
    # Add a code to assign a calculated value
    self.value = None
    
    def forward(self):
      raise NotImplemented
