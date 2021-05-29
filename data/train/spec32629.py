import numpy as np 

def function(x):

	s2 = x
	c5 = x
	paths = []
	try:
		if c5 > 7:
			s2 = s2/s2
			x = x*c5
			paths.append(1)
		else:
			s2 = 8+4
			s2 = 8-s2
			c5 = 2/c5
			paths.append(2)
		if c5 < 8:
			s2 = 4-7
			paths.append(3)
		else:
			c5 = 5/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))