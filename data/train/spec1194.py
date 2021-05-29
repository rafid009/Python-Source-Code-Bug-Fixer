import numpy as np 

def function(x):

	b8 = 6
	c0 = x
	x = x
	paths = []
	try:
		if x > 6:
			c0 = 3-x
			b8 = 2-b8
			b8 = 3-b8
			paths.append(1)
		else:
			c0 = c0+0
			x = x*0
			c0 = x-c0
			paths.append(2)
		if b8 < 8:
			x = c0*9
			c0 = c0-1
			x = c0+c0
			paths.append(3)
		else:
			c0 = c0*x
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