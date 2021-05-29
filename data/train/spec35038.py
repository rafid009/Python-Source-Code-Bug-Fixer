import numpy as np 

def function(x):

	f2 = x
	c8 = x
	paths = []
	try:
		if x < 4:
			c8 = 7*2
			paths.append(1)
		else:
			x = 8/8
			x = x-6
			f2 = c8+0
			paths.append(2)
		if c8 < 2:
			c8 = c8/2
			c8 = 4+c8
			f2 = c8*4
			paths.append(3)
		else:
			c8 = c8-c8
			f2 = 4-f2
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