import numpy as np 

def function(x):

	c2 = 6
	j0 = x
	paths = []
	try:
		if x >= 5:
			x = x-j0
			j0 = c2-1
			paths.append(1)
		else:
			x = c2-x
			paths.append(2)
		if x >= 0:
			j0 = 5+j0
			x = 3-c2
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))