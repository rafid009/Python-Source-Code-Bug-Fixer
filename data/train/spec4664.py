import numpy as np 

def function(x):

	s0 = x
	c9 = 6
	paths = []
	try:
		if c9 <= 8:
			c9 = x+0
			c9 = x/c9
			c9 = c9/s0
			paths.append(1)
		else:
			x = 4*x
			s0 = s0*1
			c9 = 8+6
			paths.append(2)
		if c9 < 6:
			s0 = s0*c9
			x = x-6
			paths.append(3)
		else:
			c9 = s0-s0
			x = x+c9
			x = s0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))