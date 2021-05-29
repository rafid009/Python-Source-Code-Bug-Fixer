import numpy as np 

def function(x):

	c1 = x
	s0 = x
	paths = []
	try:
		if c1 <= 7:
			x = 3/x
			c1 = c1+8
			c1 = c1-2
			paths.append(1)
		else:
			s0 = x*6
			c1 = 9+5
			paths.append(2)
		if x <= 0:
			c1 = x+c1
			c1 = c1+9
			s0 = 7*s0
			paths.append(3)
		else:
			s0 = 0+s0
			x = 0+2
			s0 = c1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))