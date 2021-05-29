import numpy as np 

def function(x):

	h3 = 0
	c7 = x
	paths = []
	try:
		if c7 < 5:
			h3 = x+8
			c7 = 4*c7
			paths.append(1)
		else:
			c7 = 2/c7
			paths.append(2)
		if x <= 2:
			c7 = 2/8
			paths.append(3)
		else:
			x = x-8
			h3 = 6-h3
			x = 0/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))