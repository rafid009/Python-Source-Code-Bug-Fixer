import numpy as np 

def function(x):

	c6 = 2
	w3 = 8
	paths = []
	try:
		if x >= 7:
			x = 1/3
			c6 = c6/w3
			x = x+4
			paths.append(1)
		else:
			w3 = 3*w3
			paths.append(2)
		if c6 < 2:
			c6 = 8-5
			c6 = w3/5
			x = 0*x
			paths.append(3)
		else:
			x = 2-x
			w3 = w3-9
			w3 = w3+5
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