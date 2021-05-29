import numpy as np 

def function(x):

	s2 = 6
	c0 = x
	paths = []
	try:
		if x < 5:
			c0 = 7-c0
			paths.append(1)
		else:
			c0 = c0*4
			x = s2*x
			s2 = s2/2
			paths.append(2)
		if s2 > 5:
			s2 = s2*1
			s2 = c0/s2
			s2 = s2/9
			paths.append(3)
		else:
			s2 = c0/s2
			s2 = 6/s2
			c0 = 0-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))