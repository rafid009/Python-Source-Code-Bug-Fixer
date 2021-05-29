import numpy as np 

def function(x):

	c0 = 1
	i8 = 7
	paths = []
	try:
		if x < 0:
			i8 = 6+9
			i8 = 4*i8
			paths.append(1)
		else:
			c0 = 4+c0
			i8 = x*5
			paths.append(2)
		if c0 < 7:
			x = 5*x
			i8 = i8-3
			x = 2-8
			paths.append(3)
		else:
			i8 = 0-i8
			c0 = c0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))