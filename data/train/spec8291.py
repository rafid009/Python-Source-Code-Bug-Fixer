import numpy as np 

def function(x):

	c0 = x
	u2 = x
	paths = []
	try:
		if c0 >= 1:
			u2 = 4/u2
			paths.append(1)
		else:
			c0 = 9*c0
			paths.append(2)
		if c0 >= 6:
			u2 = x-u2
			x = 8+x
			u2 = u2*c0
			paths.append(3)
		else:
			u2 = u2+0
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))