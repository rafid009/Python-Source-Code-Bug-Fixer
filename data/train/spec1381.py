import numpy as np 

def function(x):

	c2 = x
	f3 = 1
	paths = []
	try:
		if c2 > 2:
			c2 = 3+c2
			paths.append(1)
		else:
			f3 = 0-5
			x = 5+x
			paths.append(2)
		if x < 7:
			f3 = f3-3
			paths.append(3)
		else:
			c2 = 0*6
			x = x-x
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