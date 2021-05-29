import numpy as np 

def function(x):

	c2 = 2
	w3 = 1
	paths = []
	try:
		if c2 > 5:
			c2 = 3-0
			w3 = 6+8
			paths.append(1)
		else:
			c2 = 1/c2
			paths.append(2)
		if x <= 0:
			w3 = 7-w3
			c2 = c2-4
			w3 = 1-w3
			paths.append(3)
		else:
			c2 = c2/x
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