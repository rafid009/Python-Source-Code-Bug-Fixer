import numpy as np 

def function(x):

	h9 = 4
	c5 = x
	paths = []
	try:
		if x < 2:
			x = x-h9
			c5 = c5-8
			paths.append(1)
		else:
			c5 = c5*6
			x = x*x
			paths.append(2)
		if c5 >= 9:
			h9 = x/3
			paths.append(3)
		else:
			c5 = c5+8
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