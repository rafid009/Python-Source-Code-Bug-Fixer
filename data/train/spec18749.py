import numpy as np 

def function(x):

	l9 = 1
	c5 = 6
	paths = []
	try:
		if c5 > 1:
			l9 = l9-c5
			c5 = c5-0
			x = 1-x
			paths.append(1)
		else:
			c5 = c5+7
			paths.append(2)
		if l9 < 1:
			c5 = c5+x
			c5 = c5*4
			paths.append(3)
		else:
			x = x*c5
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