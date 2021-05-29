import numpy as np 

def function(x):

	c8 = 3
	l6 = x
	paths = []
	try:
		if c8 < 1:
			l6 = l6-6
			x = 6-3
			c8 = 2+l6
			paths.append(1)
		else:
			c8 = 8/8
			l6 = l6-3
			c8 = x-c8
			paths.append(2)
		if c8 <= 3:
			l6 = x-c8
			l6 = l6+3
			paths.append(3)
		else:
			l6 = l6*9
			x = 2*9
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