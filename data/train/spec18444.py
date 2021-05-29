import numpy as np 

def function(x):

	c0 = x
	b8 = x
	paths = []
	try:
		if b8 < 9:
			x = 7/c0
			paths.append(1)
		else:
			x = x-4
			c0 = 9*b8
			x = 5+0
			paths.append(2)
		if c0 < 7:
			b8 = b8-b8
			b8 = 3/c0
			x = x*x
			paths.append(3)
		else:
			x = b8+0
			x = x*6
			b8 = 7/5
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))