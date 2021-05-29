import numpy as np 

def function(x):

	e4 = 8
	c5 = x
	paths = []
	try:
		if c5 < 0:
			x = 8+x
			c5 = c5/e4
			paths.append(1)
		else:
			x = 5*2
			paths.append(2)
		if c5 >= 8:
			e4 = e4/2
			c5 = e4-c5
			x = 1-x
			paths.append(3)
		else:
			e4 = c5-e4
			x = x-4
			c5 = 4/9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		c5 = e4**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))