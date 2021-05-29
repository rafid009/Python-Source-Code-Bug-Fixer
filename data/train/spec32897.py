import numpy as np 

def function(x):

	s6 = 3
	c2 = 8
	paths = []
	try:
		if s6 >= 7:
			c2 = c2-4
			c2 = c2-s6
			paths.append(1)
		else:
			s6 = s6-6
			paths.append(2)
		if s6 <= 3:
			c2 = 0-4
			s6 = 8/x
			x = 1*x
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))