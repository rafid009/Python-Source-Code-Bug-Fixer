import numpy as np 

def function(x):

	s0 = 3
	c9 = 5
	x = 5
	paths = []
	try:
		if x <= 5:
			x = 7-s0
			s0 = 0-s0
			x = x/7
			paths.append(1)
		else:
			c9 = c9*0
			s0 = x-s0
			paths.append(2)
		if s0 > 4:
			x = x+5
			x = 1/1
			s0 = s0*6
			paths.append(3)
		else:
			s0 = 6-3
			x = 1-4
			s0 = s0-s0
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