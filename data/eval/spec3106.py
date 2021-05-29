import numpy as np 

def function(x):

	c5 = 4
	h4 = x
	paths = []
	try:
		if c5 < 7:
			h4 = 1*6
			h4 = h4+c5
			paths.append(1)
		else:
			h4 = x*h4
			h4 = h4*x
			c5 = c5/h4
			paths.append(2)
		if c5 <= 4:
			x = x-2
			c5 = c5*8
			paths.append(3)
		else:
			c5 = c5-h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))