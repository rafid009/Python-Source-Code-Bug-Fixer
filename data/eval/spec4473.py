import numpy as np 

def function(x):

	c0 = 7
	e3 = x
	paths = []
	try:
		if c0 <= 1:
			c0 = e3+c0
			x = 7+x
			paths.append(1)
		else:
			x = c0+x
			c0 = 3-c0
			x = c0*6
			paths.append(2)
		if c0 > 9:
			x = 0*x
			c0 = x+c0
			paths.append(3)
		else:
			c0 = 7+c0
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