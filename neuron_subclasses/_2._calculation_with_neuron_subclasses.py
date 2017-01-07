
# create a neuron subclass to perform addition
class Add(Neuron):
  
  # Instantiate all the values
  def __init__(self,x,y):
    Neuron.__init__(self, [x,y])
    
  # Create a code to perform forward propagation
  
