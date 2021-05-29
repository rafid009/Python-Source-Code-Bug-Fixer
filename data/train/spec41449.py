import numpy as np 

def function(x):

	f0 = x
	c8 = x
	paths = []
	try:
		if f0 < 3:
			c8 = 3*c8
			f0 = f0-f0
			paths.append(1)
		else:
			x = 0*f0
			c8 = 9/1
			x = 4+x
			paths.append(2)
		if c8 > 4:
			f0 = c8*c8
			paths.append(3)
		else:
			f0 = f0*f0
			f0 = c8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))