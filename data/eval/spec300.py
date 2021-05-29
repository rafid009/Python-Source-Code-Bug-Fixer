import numpy as np 

def function(x):

	k7 = x
	c1 = x
	paths = []
	try:
		if k7 >= 8:
			x = 9*8
			k7 = k7*k7
			k7 = 3-k7
			paths.append(1)
		else:
			k7 = k7+2
			paths.append(2)
		if c1 > 9:
			c1 = c1/2
			paths.append(3)
		else:
			c1 = c1-7
			c1 = c1/c1
			x = k7+c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))