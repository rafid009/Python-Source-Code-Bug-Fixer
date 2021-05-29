import numpy as np 

def function(x):

	f9 = x
	c4 = 2
	paths = []
	try:
		if f9 < 2:
			f9 = c4*4
			paths.append(1)
		else:
			c4 = 2/c4
			paths.append(2)
		if c4 >= 4:
			c4 = f9/c4
			f9 = f9+c4
			x = x+2
			paths.append(3)
		else:
			c4 = c4/7
			f9 = 1*7
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