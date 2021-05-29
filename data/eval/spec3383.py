import numpy as np 

def function(x):

	c6 = x
	x1 = 9
	paths = []
	try:
		if c6 < 8:
			x1 = 6*x1
			paths.append(1)
		else:
			x1 = 8-x1
			x = x*1
			x = x1*3
			paths.append(2)
		if x1 < 6:
			c6 = 1-6
			paths.append(3)
		else:
			c6 = c6+9
			x = 9/x
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