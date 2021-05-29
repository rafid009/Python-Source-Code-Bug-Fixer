import numpy as np 

def function(x):

	c9 = x
	k4 = 7
	x = 5
	paths = []
	try:
		if c9 >= 8:
			x = 8*x
			k4 = c9/k4
			c9 = 9-k4
			paths.append(1)
		else:
			c9 = c9+9
			x = k4-2
			paths.append(2)
		if k4 <= 1:
			k4 = x*9
			k4 = 3*c9
			paths.append(3)
		else:
			k4 = c9/7
			x = c9*x
			x = 1/x
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