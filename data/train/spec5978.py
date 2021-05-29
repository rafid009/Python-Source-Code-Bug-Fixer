import numpy as np 

def function(x):

	x1 = x
	c8 = x
	paths = []
	try:
		if x1 <= 9:
			x1 = 8-x1
			x1 = x1*c8
			x = c8*x
			paths.append(1)
		else:
			c8 = 4/c8
			paths.append(2)
		if x1 >= 6:
			x = c8/1
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))