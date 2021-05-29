import numpy as np 

def function(x):

	s2 = x
	c1 = x
	paths = []
	try:
		if s2 >= 9:
			s2 = s2/5
			paths.append(1)
		else:
			c1 = c1/s2
			s2 = 2*s2
			paths.append(2)
		if x > 0:
			c1 = 7+3
			paths.append(3)
		else:
			x = 5-0
			s2 = s2/2
			s2 = 7+s2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		c1 = s2**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))