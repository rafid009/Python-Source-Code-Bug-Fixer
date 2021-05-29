import numpy as np 

def function(x):

	l4 = x
	c9 = x
	paths = []
	try:
		if c9 < 7:
			c9 = c9+2
			paths.append(1)
		else:
			l4 = l4-x
			c9 = 9+2
			paths.append(2)
		if c9 >= 3:
			x = 2/x
			paths.append(3)
		else:
			l4 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))