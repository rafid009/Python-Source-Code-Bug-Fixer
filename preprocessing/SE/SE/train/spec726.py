import numpy as np 

def function(x):

	w0 = x
	c6 = 5
	paths = []
	try:
		if c6 > 9:
			x = x/w0
			x = w0+2
			paths.append(1)
		else:
			c6 = 5+0
			x = w0*4
			paths.append(2)
		if x > 6:
			x = x/c6
			paths.append(3)
		else:
			x = w0-x
			w0 = 8/w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))