import numpy as np 

def function(x):

	c2 = 7
	a3 = 6
	paths = []
	try:
		if a3 > 9:
			c2 = 3/3
			c2 = 2*c2
			paths.append(1)
		else:
			a3 = a3*6
			c2 = 0-1
			paths.append(2)
		if a3 < 1:
			c2 = c2/2
			c2 = 8-2
			a3 = 4/a3
			paths.append(3)
		else:
			c2 = 8-x
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