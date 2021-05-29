import numpy as np 

def function(x):

	h8 = 4
	c4 = x
	paths = []
	try:
		if c4 < 9:
			h8 = x*0
			h8 = 2*4
			h8 = h8-h8
			paths.append(1)
		else:
			c4 = 3*c4
			x = x-3
			paths.append(2)
		if x >= 7:
			x = 7+9
			x = x+6
			h8 = h8-3
			paths.append(3)
		else:
			c4 = c4*c4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))