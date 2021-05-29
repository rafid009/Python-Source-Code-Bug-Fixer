import numpy as np 

def function(x):

	e3 = 2
	c8 = 8
	x = 4
	paths = []
	try:
		if e3 < 7:
			e3 = x-e3
			c8 = 0+c8
			x = x*7
			paths.append(1)
		else:
			e3 = 0*x
			paths.append(2)
		if c8 <= 1:
			e3 = 7+0
			c8 = c8+8
			x = 8-x
			paths.append(3)
		else:
			x = 1-x
			e3 = e3+e3
			x = 5+x
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