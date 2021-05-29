import numpy as np 

def function(x):

	h4 = x
	c0 = 9
	paths = []
	try:
		if c0 >= 4:
			h4 = h4-8
			x = x/3
			paths.append(1)
		else:
			c0 = c0*7
			x = 4+3
			paths.append(2)
		if h4 >= 6:
			c0 = 5+h4
			c0 = h4/c0
			x = x*0
			paths.append(3)
		else:
			h4 = 2*h4
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