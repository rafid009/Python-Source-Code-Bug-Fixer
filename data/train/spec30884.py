import numpy as np 

def function(x):

	c4 = 7
	x1 = x
	paths = []
	try:
		if x < 7:
			x1 = x1/x1
			c4 = 3/7
			x = x/x
			paths.append(1)
		else:
			x1 = 1-x1
			x = 8/x
			x = c4-8
			paths.append(2)
		if x <= 2:
			x = c4-5
			paths.append(3)
		else:
			x1 = x1/x1
			x = x1/x
			x = x*3
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