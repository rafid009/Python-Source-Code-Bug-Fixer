import numpy as np 

def function(x):

	s2 = 6
	c5 = 2
	paths = []
	try:
		if x <= 3:
			c5 = s2+6
			c5 = 3*c5
			paths.append(1)
		else:
			x = 1+9
			c5 = c5-0
			paths.append(2)
		if c5 <= 1:
			x = x*s2
			s2 = 4-s2
			paths.append(3)
		else:
			s2 = 5/s2
			s2 = 1/s2
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