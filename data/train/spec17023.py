import numpy as np 

def function(x):

	h3 = x
	c9 = 1
	paths = []
	try:
		if x < 9:
			x = 1+x
			paths.append(1)
		else:
			h3 = h3*h3
			x = 4+c9
			paths.append(2)
		if x <= 7:
			x = x-c9
			h3 = h3-8
			paths.append(3)
		else:
			h3 = h3*3
			x = 4/c9
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))