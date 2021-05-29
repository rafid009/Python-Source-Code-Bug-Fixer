import numpy as np 

def function(x):

	x0 = 2
	c5 = 7
	paths = []
	try:
		if c5 > 2:
			x = x-5
			paths.append(1)
		else:
			x = x-5
			c5 = 1-0
			paths.append(2)
		if c5 > 1:
			c5 = 3-c5
			x = x*2
			paths.append(3)
		else:
			x0 = x0/x0
			x = 2/x
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