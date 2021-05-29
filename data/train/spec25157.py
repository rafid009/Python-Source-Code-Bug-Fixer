import numpy as np 

def function(x):

	c2 = x
	b3 = 2
	paths = []
	try:
		if b3 < 2:
			c2 = 1-x
			paths.append(1)
		else:
			c2 = x/c2
			b3 = b3-b3
			b3 = b3-b3
			paths.append(2)
		if b3 > 3:
			c2 = 4+3
			paths.append(3)
		else:
			c2 = x+c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))