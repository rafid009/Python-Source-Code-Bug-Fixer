import numpy as np 

def function(x):

	c0 = 2
	h4 = 8
	paths = []
	try:
		if x > 1:
			h4 = h4+c0
			paths.append(1)
		else:
			x = 3+x
			h4 = x+0
			paths.append(2)
		if c0 >= 6:
			c0 = 9*2
			paths.append(3)
		else:
			x = x+x
			c0 = x*3
			h4 = 8/h4
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