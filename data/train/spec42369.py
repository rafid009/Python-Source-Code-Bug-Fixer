import numpy as np 

def function(x):

	l5 = 8
	c6 = x
	x = 4
	paths = []
	try:
		if c6 <= 6:
			c6 = c6*x
			paths.append(1)
		else:
			c6 = 4+c6
			x = 1/x
			l5 = 3+l5
			paths.append(2)
		if c6 < 4:
			x = c6*x
			paths.append(3)
		else:
			x = 6*x
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