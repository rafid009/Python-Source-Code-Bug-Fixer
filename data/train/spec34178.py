import numpy as np 

def function(x):

	c6 = 4
	l0 = 1
	paths = []
	try:
		if x < 4:
			c6 = c6+5
			c6 = 9+c6
			paths.append(1)
		else:
			l0 = l0-x
			paths.append(2)
		if x > 4:
			l0 = 9/6
			x = x-9
			paths.append(3)
		else:
			l0 = 2*x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		c6 = l0**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))