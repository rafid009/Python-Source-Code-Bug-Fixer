import numpy as np 

def function(x):

	c5 = x
	q2 = 5
	paths = []
	try:
		if x >= 5:
			c5 = c5-9
			q2 = c5+6
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x > 3:
			x = x/1
			paths.append(3)
		else:
			c5 = c5*x
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