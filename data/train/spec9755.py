import numpy as np 

def function(x):

	c0 = 5
	y6 = x
	paths = []
	try:
		if y6 > 0:
			c0 = c0+9
			y6 = 8*y6
			x = 3/x
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if c0 <= 3:
			c0 = c0+6
			paths.append(3)
		else:
			c0 = c0/5
			c0 = x*c0
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