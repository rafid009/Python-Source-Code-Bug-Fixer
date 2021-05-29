import numpy as np 

def function(x):

	c3 = 4
	s2 = 3
	paths = []
	try:
		if s2 <= 8:
			x = 5*x
			x = c3-x
			s2 = 4-s2
			paths.append(1)
		else:
			c3 = 5/4
			x = 2*x
			s2 = s2/s2
			paths.append(2)
		if c3 < 1:
			s2 = 0/s2
			c3 = 2/8
			paths.append(3)
		else:
			s2 = x-7
			s2 = 4-s2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))