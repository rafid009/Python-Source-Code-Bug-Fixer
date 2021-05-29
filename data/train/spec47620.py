import numpy as np 

def function(x):

	l4 = 3
	c6 = 5
	paths = []
	try:
		if x < 9:
			x = 1-l4
			l4 = l4-4
			c6 = c6+1
			paths.append(1)
		else:
			c6 = c6/4
			c6 = c6-6
			x = 9/7
			paths.append(2)
		if l4 <= 9:
			c6 = 9*c6
			c6 = 4-c6
			paths.append(3)
		else:
			c6 = l4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))