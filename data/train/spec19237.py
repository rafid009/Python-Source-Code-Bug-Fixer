import numpy as np 

def function(x):

	c3 = 2
	x2 = x
	paths = []
	try:
		if x >= 7:
			x2 = x2+8
			paths.append(1)
		else:
			x2 = 9-x2
			c3 = 1-6
			paths.append(2)
		if x >= 3:
			x2 = 8+c3
			paths.append(3)
		else:
			x = c3*8
			x2 = c3-9
			x = 7/x
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