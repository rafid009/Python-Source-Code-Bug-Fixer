import numpy as np 

def function(x):

	s6 = 7
	c5 = 0
	paths = []
	try:
		if s6 >= 7:
			s6 = s6*1
			c5 = c5-8
			paths.append(1)
		else:
			s6 = 1-s6
			s6 = 8-1
			c5 = c5*6
			paths.append(2)
		if c5 > 7:
			s6 = 4*9
			s6 = c5-x
			paths.append(3)
		else:
			x = 2+x
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