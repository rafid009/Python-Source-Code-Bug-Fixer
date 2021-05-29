import numpy as np 

def function(x):

	c4 = 5
	q3 = x
	paths = []
	try:
		if c4 < 2:
			q3 = 4-q3
			paths.append(1)
		else:
			c4 = c4-5
			c4 = q3+c4
			x = x*4
			paths.append(2)
		if q3 > 8:
			c4 = 1*8
			c4 = c4-7
			paths.append(3)
		else:
			c4 = 4*c4
			c4 = c4/c4
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