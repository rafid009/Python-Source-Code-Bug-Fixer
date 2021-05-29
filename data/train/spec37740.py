import numpy as np 

def function(x):

	c4 = x
	h6 = x
	paths = []
	try:
		if x <= 9:
			h6 = h6*x
			paths.append(1)
		else:
			c4 = c4*0
			paths.append(2)
		if h6 >= 7:
			h6 = 0/h6
			h6 = h6*8
			paths.append(3)
		else:
			h6 = x-h6
			x = 2/h6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))