import numpy as np 

def function(x):

	c0 = 7
	w5 = 3
	paths = []
	try:
		if c0 < 6:
			w5 = 5-w5
			paths.append(1)
		else:
			c0 = c0+9
			x = 6/x
			x = x+4
			paths.append(2)
		if c0 < 4:
			c0 = c0-9
			paths.append(3)
		else:
			w5 = w5+c0
			w5 = 0-w5
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