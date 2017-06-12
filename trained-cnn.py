class  ComputationalGragh(object):
	"""docstring for  ComputationalGragh"""
	def __init__(self, arg):
		super  ComputationalGragh, self).__init__()
		self.arg = arg

	def forward(imputs):

		for gate in self.gragh.nodes_topologically_sorted():
			gate.forwar()
		return loss

	def backward():
		for gate in self.gragh.nodes_topologically_sorted():
			gate.backward()
			return inputs_gradients

		

class MultiplyGate(object)：
    def forward(x, y)
        z = x * y
        self.x = x
        self.y = y
        return z

    def backward(dz)
    	dx = self.y * dz
    	dy = self.x * dz
    	return [dx , dy]


class AddGate(object)：
    def forward(x, y)
        z = x + y
        self.x = x
        self.y = y
        return z

    def backward(dz)
    	dx =  dz
    	dy =  dz
    	return [dx , dy]

class MaxGate(object)：
    def forward(x, y)
        z = Mamium(x , y)   
        self.x = x
        self.y = y          	
        return z

    def backward(dz)
    	if x > y
    		dx = self.y * dz
    		dy = 0
    	else 
    		dy = self.x *dz
    		dx = 0
      	return [dx , dy]