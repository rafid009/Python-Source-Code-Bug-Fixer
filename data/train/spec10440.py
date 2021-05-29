import numpy as np 

def function(x):

	b1 = 2
	c8 = 4
	paths = []
	try:
		if x > 6:
			b1 = b1/8
			paths.append(1)
		else:
			x = x+9
			c8 = 9/b1
			b1 = b1+c8
			paths.append(2)
		if x < 0:
			c8 = 1-x
			c8 = c8+b1
			b1 = 0+b1
			paths.append(3)
		else:
			b1 = 3*3
			b1 = b1-4
			b1 = c8/b1
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