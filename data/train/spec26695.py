import numpy as np 

def function(x):

	b3 = 0
	c9 = 6
	paths = []
	try:
		if b3 > 7:
			x = x-x
			paths.append(1)
		else:
			b3 = b3*x
			b3 = b3/5
			b3 = 5*b3
			paths.append(2)
		if x < 9:
			c9 = b3-c9
			b3 = x*b3
			paths.append(3)
		else:
			x = c9+b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))