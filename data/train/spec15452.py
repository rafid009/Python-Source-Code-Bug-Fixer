import numpy as np 

def function(x):

	c0 = 8
	l6 = x
	paths = []
	try:
		if c0 >= 1:
			x = 5-x
			l6 = 2/c0
			l6 = 8/l6
			paths.append(1)
		else:
			x = 1/l6
			x = 8+5
			paths.append(2)
		if c0 <= 0:
			c0 = x+c0
			paths.append(3)
		else:
			l6 = l6/4
			c0 = 6/x
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