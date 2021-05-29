import numpy as np 

def function(x):

	c5 = x
	w4 = 2
	paths = []
	try:
		if w4 < 8:
			c5 = 1-c5
			w4 = w4-c5
			w4 = 9-w4
			paths.append(1)
		else:
			w4 = w4+2
			c5 = c5*0
			c5 = c5/x
			paths.append(2)
		if x >= 3:
			c5 = c5+c5
			w4 = w4-7
			w4 = 6/x
			paths.append(3)
		else:
			c5 = c5/4
			w4 = 3+w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))