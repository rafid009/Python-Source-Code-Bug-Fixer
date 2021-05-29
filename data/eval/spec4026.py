import numpy as np 

def function(x):

	c9 = x
	w4 = x
	x = 3
	paths = []
	try:
		if w4 <= 8:
			c9 = c9*w4
			c9 = 0-x
			paths.append(1)
		else:
			c9 = c9-c9
			x = x/2
			paths.append(2)
		if c9 >= 8:
			c9 = c9*x
			w4 = w4-6
			x = c9-w4
			paths.append(3)
		else:
			c9 = 2*c9
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))