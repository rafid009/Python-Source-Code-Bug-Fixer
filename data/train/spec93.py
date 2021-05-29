import numpy as np 

def function(x):

	c0 = 8
	r1 = 4
	paths = []
	try:
		if c0 > 8:
			c0 = c0*3
			c0 = c0/8
			paths.append(1)
		else:
			r1 = r1/8
			paths.append(2)
		if x >= 6:
			r1 = 9+r1
			r1 = 3/4
			paths.append(3)
		else:
			c0 = 5-6
			c0 = c0-5
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