import numpy as np 

def function(x):

	s0 = 1
	c5 = 2
	paths = []
	try:
		if x > 5:
			x = 8+x
			paths.append(1)
		else:
			s0 = s0-6
			s0 = c5/c5
			x = 1*x
			paths.append(2)
		if x >= 7:
			c5 = c5/2
			c5 = 1/c5
			s0 = x*1
			paths.append(3)
		else:
			c5 = x+7
			c5 = c5*9
			s0 = s0+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))