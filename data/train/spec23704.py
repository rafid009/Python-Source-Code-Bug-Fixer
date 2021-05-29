import numpy as np 

def function(x):

	l9 = x
	c9 = 9
	paths = []
	try:
		if c9 < 6:
			c9 = c9/l9
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if c9 < 7:
			c9 = c9*9
			c9 = 9*7
			paths.append(3)
		else:
			x = c9/x
			l9 = l9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))