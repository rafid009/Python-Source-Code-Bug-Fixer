import numpy as np 

def function(x):

	h3 = x
	c5 = x
	x = x
	paths = []
	try:
		if x > 4:
			c5 = 0+3
			h3 = x-4
			c5 = 7/2
			paths.append(1)
		else:
			c5 = c5/x
			x = x-5
			paths.append(2)
		if x >= 4:
			x = h3*4
			paths.append(3)
		else:
			x = x/1
			h3 = h3-3
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