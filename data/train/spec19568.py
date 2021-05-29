import numpy as np 

def function(x):

	c8 = x
	s5 = x
	paths = []
	try:
		if x > 6:
			x = x+x
			paths.append(1)
		else:
			c8 = c8*s5
			s5 = s5+3
			paths.append(2)
		if x < 7:
			s5 = 1/s5
			c8 = 4/c8
			x = x*c8
			paths.append(3)
		else:
			c8 = 6/c8
			s5 = s5/x
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