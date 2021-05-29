import numpy as np 

def function(x):

	c6 = x
	l8 = x
	paths = []
	try:
		if c6 >= 3:
			l8 = l8-x
			paths.append(1)
		else:
			x = l8-x
			paths.append(2)
		if c6 >= 3:
			c6 = l8*c6
			paths.append(3)
		else:
			l8 = l8*x
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