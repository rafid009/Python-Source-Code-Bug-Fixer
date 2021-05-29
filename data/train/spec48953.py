import numpy as np 

def function(x):

	i0 = x
	c7 = 5
	paths = []
	try:
		if x > 6:
			x = 1*0
			c7 = c7/4
			c7 = c7/i0
			paths.append(1)
		else:
			i0 = 6/2
			i0 = x-2
			paths.append(2)
		if c7 >= 0:
			c7 = x-4
			paths.append(3)
		else:
			i0 = i0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))