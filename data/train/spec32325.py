import numpy as np 

def function(x):

	c2 = x
	w3 = 9
	x = x
	paths = []
	try:
		if x > 2:
			c2 = w3/4
			w3 = w3/4
			paths.append(1)
		else:
			c2 = 0*c2
			w3 = w3+2
			c2 = w3-5
			paths.append(2)
		if x > 8:
			x = 1-x
			paths.append(3)
		else:
			x = 4/x
			c2 = x+c2
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