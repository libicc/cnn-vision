

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
