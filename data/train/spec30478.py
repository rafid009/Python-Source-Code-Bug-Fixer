import numpy as np 

def function(x):

	a0 = 9
	c4 = x
	paths = []
	try:
		if x > 1:
			x = x-0
			paths.append(1)
		else:
			c4 = 5+c4
			paths.append(2)
		if c4 < 7:
			x = x+4
			x = 6+x
			paths.append(3)
		else:
			c4 = c4+9
			c4 = 0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))