import numpy as np 

def function(x):

	c4 = x
	k2 = x
	paths = []
	try:
		if c4 < 5:
			x = 7+k2
			x = 1-x
			x = 8+x
			paths.append(1)
		else:
			k2 = 7/k2
			k2 = k2-3
			paths.append(2)
		if c4 <= 0:
			c4 = c4*c4
			c4 = c4*8
			c4 = 1-c4
			paths.append(3)
		else:
			c4 = c4*9
			c4 = 0-x
			c4 = 0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))