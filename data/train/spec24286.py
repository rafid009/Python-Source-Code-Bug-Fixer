import numpy as np 

def function(x):

	c6 = x
	a6 = 4
	paths = []
	try:
		if c6 >= 7:
			x = 4-x
			paths.append(1)
		else:
			a6 = a6/a6
			x = 2*x
			c6 = c6/x
			paths.append(2)
		if c6 <= 8:
			c6 = 6*c6
			c6 = 6*c6
			paths.append(3)
		else:
			a6 = a6/8
			c6 = 6/c6
			c6 = 1-3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))