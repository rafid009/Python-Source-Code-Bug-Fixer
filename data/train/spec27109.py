import numpy as np 

def function(x):

	s9 = 4
	c9 = 6
	paths = []
	try:
		if x <= 9:
			c9 = c9/3
			x = x-9
			paths.append(1)
		else:
			c9 = c9-3
			s9 = s9+2
			paths.append(2)
		if c9 > 1:
			c9 = c9-0
			c9 = 2*c9
			x = 5/x
			paths.append(3)
		else:
			x = x/3
			s9 = 0+c9
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