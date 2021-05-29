import numpy as np 

def function(x):

	k1 = x
	c4 = x
	paths = []
	try:
		if x >= 6:
			c4 = 1-c4
			paths.append(1)
		else:
			k1 = 1-8
			paths.append(2)
		if c4 >= 8:
			k1 = x/k1
			x = x*3
			paths.append(3)
		else:
			c4 = c4*2
			c4 = 2*c4
			x = x+x
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