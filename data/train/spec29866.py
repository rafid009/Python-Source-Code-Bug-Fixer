import numpy as np 

def function(x):

	s7 = 6
	c1 = 4
	paths = []
	try:
		if s7 < 9:
			c1 = 2/c1
			c1 = 9-3
			c1 = c1*c1
			paths.append(1)
		else:
			s7 = s7/6
			s7 = 7+s7
			x = 9*x
			paths.append(2)
		if c1 >= 6:
			c1 = 6*9
			s7 = c1-c1
			s7 = 7*x
			paths.append(3)
		else:
			s7 = 4-6
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))