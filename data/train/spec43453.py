import numpy as np 

def function(x):

	c8 = x
	h3 = 8
	paths = []
	try:
		if c8 <= 8:
			h3 = h3/9
			paths.append(1)
		else:
			x = h3*x
			paths.append(2)
		if h3 < 1:
			x = c8+6
			paths.append(3)
		else:
			c8 = h3*4
			x = x+h3
			x = 4/x
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