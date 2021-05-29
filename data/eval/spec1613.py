import numpy as np 

def function(x):

	c9 = 6
	q3 = 4
	paths = []
	try:
		if x <= 1:
			x = 1+x
			c9 = 4+6
			q3 = q3-2
			paths.append(1)
		else:
			x = x-3
			q3 = c9*8
			paths.append(2)
		if q3 <= 9:
			c9 = x/c9
			x = x-c9
			q3 = q3-7
			paths.append(3)
		else:
			q3 = q3/9
			c9 = c9*c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))