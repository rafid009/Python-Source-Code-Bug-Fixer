import numpy as np 

def function(x):

	c8 = x
	k7 = 5
	paths = []
	try:
		if x >= 1:
			x = 9+x
			x = c8*x
			k7 = 1-4
			paths.append(1)
		else:
			c8 = 9-k7
			paths.append(2)
		if c8 >= 1:
			x = 7-6
			c8 = c8+0
			paths.append(3)
		else:
			c8 = 4*x
			k7 = 4+6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))