import numpy as np 

def function(x):

	c4 = x
	w4 = 4
	paths = []
	try:
		if w4 < 3:
			w4 = 9/c4
			w4 = 0*w4
			paths.append(1)
		else:
			w4 = w4-3
			paths.append(2)
		if x >= 2:
			x = 4/x
			c4 = c4-w4
			x = 5-w4
			paths.append(3)
		else:
			x = 4/x
			w4 = c4/w4
			x = x/5
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