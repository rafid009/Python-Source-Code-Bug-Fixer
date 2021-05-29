import numpy as np 

def function(x):

	s2 = x
	c4 = 8
	x = x
	paths = []
	try:
		if x >= 3:
			s2 = 8-s2
			c4 = 3/s2
			paths.append(1)
		else:
			x = 1-4
			x = 7-x
			c4 = c4*2
			paths.append(2)
		if s2 >= 0:
			x = 2/1
			s2 = s2*c4
			paths.append(3)
		else:
			s2 = s2*c4
			x = 0+s2
			c4 = c4-0
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))